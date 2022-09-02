from app import db, login
from flask_login import UserMixin
from initial_data import _HANDICAPS_, _HANDICAP_INDICES_NINE_HOLES_, _PLAYERS_, _TEAMS_, _MEN_COURSE_HDCP_, _WOMEN_COURSE_HDCP_
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) if password is not None else None

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) if self.password_hash is not None else False

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tee = db.Column(db.String(10))
    hdcp_index_nine = db.Column(db.String(4))  # max 3 digits + "." -> 10.4
    hdcp_front = db.Column(db.Integer)
    hdcp_back = db.Column(db.Integer)
    hdcp_total = db.Column(db.Integer)
    hdcp_per_hole = db.Column(db.String(64))
    front_score = db.Column(db.Integer)
    front_net_score = db.Column(db.Integer)
    back_score = db.Column(db.Integer)
    back_net_score = db.Column(db.Integer)
    total_score = db.Column(db.Integer)
    total_net_score = db.Column(db.Integer)
    hole1 = db.Column(db.Integer)
    hole2 = db.Column(db.Integer)
    hole3 = db.Column(db.Integer)
    hole4 = db.Column(db.Integer)
    hole5 = db.Column(db.Integer)
    hole6 = db.Column(db.Integer)
    hole7 = db.Column(db.Integer)
    hole8 = db.Column(db.Integer)
    hole9 = db.Column(db.Integer)
    hole10 = db.Column(db.Integer)
    hole11 = db.Column(db.Integer)
    hole12 = db.Column(db.Integer)
    hole13 = db.Column(db.Integer)
    hole14 = db.Column(db.Integer)
    hole15 = db.Column(db.Integer)
    hole16 = db.Column(db.Integer)
    hole17 = db.Column(db.Integer)
    hole18 = db.Column(db.Integer)

    def set_hdcp_per_hole(self, hdcp_per_hole):
        if type(hdcp_per_hole) is list:
            holes_str = [str(i) for i in hdcp_per_hole]
            self.hdcp_per_hole = ' '.join(holes_str)
        elif type(hdcp_per_hole) is str:
            self.hdcp_per_hole = hdcp_per_hole
        else:
            raise Exception('Invalid type for hdcp_per_hole in Player')

    def get_hdcp_per_hole(self):
        return [int(i) for i in self.hdcp_per_hole.split(' ')]

    def __repr__(self):
        return '<{} Player {}; Team {}>'.format(self.id, self.name, self.team_id)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    player_one = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_two = db.Column(db.Integer, db.ForeignKey('player.id'))
    foursome = db.Column(db.Integer)

    def __repr__(self):
        return '<{} Team {}>'.format(self.id, self.name)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def init_users():
    users = User.query.all()
    if users is None or len(users) == 0:
        print("Adding all users")
        for name, username, email, tee in _PLAYERS_:
            print("Adding user {}".format(name))
            user = User(username=username, email=email, role='user')
            db.session.add(user)
        db.session.add(User(username='admin', email='kmueller+admin@bluecedar.com', role='admin'))
        db.session.commit()


def init_players():
    players = Player.query.all()
    if players is None or len(players) == 0:
        print("Adding all players")
        for name, username, email, tee in _PLAYERS_:
            print("Adding player {}".format(name))
            user = User.query.filter_by(username=username).first()
            if user is None:
                raise Exception('User not found in user table with username "{}"'.format(username))
            hdcp_front = _HANDICAPS_[name][0]
            hdcp_back = _HANDICAPS_[name][1]
            hdcp_total = hdcp_front + hdcp_back
            hdcp_index_nine = str(_HANDICAP_INDICES_NINE_HOLES_[name])
            player = Player(name=name, user_id=user.id, hdcp_front=hdcp_front, hdcp_back=hdcp_back, hdcp_total=hdcp_total,
                            hdcp_index_nine=hdcp_index_nine, tee=tee)
            db.session.add(player)
        db.session.commit()


def init_teams():
    teams = Team.query.all()
    if teams is None or len(teams) == 0:
        print("Adding all teams")
        for name, players_and_foursome in _TEAMS_.items():
            print("Adding team {}".format(name))
            p1 = Player.query.filter_by(name=players_and_foursome[0]).first()
            p2 = Player.query.filter_by(name=players_and_foursome[1]).first()
            foursome = players_and_foursome[2]
            team = Team(name=name, player_one=p1.id, player_two=p2.id, foursome=foursome)
            db.session.add(team)
            print("p1 {} - team {}".format(p1, p1.team_id))
            # commit to DB so we get an id from the entry
            db.session.commit()
            p1.team_id = team.id
            p2.team_id = team.id
            print("p1 {} - team {}".format(p1, p1.team_id))
            # commit so we don't lose the player data on the next loop?
            db.session.commit()


def hole_hdcp_for_player(player):
    print('Calculating hole handicaps for player {}'.format(player.name))
    hdcp_total = player.hdcp_total
    hole_idx = 0
    holes = [0] * 18
    while hole_idx < hdcp_total:
        # find which handicap number to edit - hole_idx mod 18. Starting at hardest hole to easiest
        hdcp_to_edit = (hole_idx % 18)
        # find which hole to modify the hdcp for. hdcp_to_edit is 0 based and the course handicap numbers are 1
        # based, so add 1
        if player.tee == 'red':
            course_hdcps = _WOMEN_COURSE_HDCP_
        else:
            course_hdcps = _MEN_COURSE_HDCP_
        hole_to_edit = course_hdcps.index(hdcp_to_edit + 1)
        holes[hole_to_edit] += 1
        hole_idx += 1

    print('hole hdcps {}'.format(holes))
    return holes


def init_per_hole_hdcp():
    # Calculate hole handicaps for the champ group
    from app.scoring import get_foursome
    team1, team2, p1, p2, p3, p4 = get_foursome(5)
    p1.set_hdcp_per_hole(hole_hdcp_for_player(p1))
    p2.set_hdcp_per_hole(hole_hdcp_for_player(p2))
    p3.set_hdcp_per_hole(hole_hdcp_for_player(p3))
    p4.set_hdcp_per_hole(hole_hdcp_for_player(p4))
    db.session.commit()


def init_defaults():
    """Pre-Populate Tables"""
    init_users()
    init_players()
    init_teams()
    init_per_hole_hdcp()
