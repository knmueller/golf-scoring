from app import db, login
from flask_login import UserMixin
from initial_data import _HANDICAPS_, _HANDICAP_INDICES_NINE_HOLES_, _PLAYERS_, _TEAMS_
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # player_id ?
    # team_id ?

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) if self.password_hash is not None else False

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    hdcp_index_nine = db.Column(db.String(4))  # max 3 digits + "." -> 10.4
    hdcp_front = db.Column(db.Integer)
    hdcp_back = db.Column(db.Integer)
    hdcp_total = db.Column(db.Integer)
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

    def __repr__(self):
        return '<{} Player {}>'.format(self.id, self.name)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    player_one = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_two = db.Column(db.Integer, db.ForeignKey('player.id'))

    def __repr__(self):
        return '<{} Team {}>'.format(self.id, self.name)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def init_users():
    users = User.query.all()
    if users is None or len(users) == 0:
        print("Adding all users")
        for name, username, email, role in _PLAYERS_:
            print("Adding user {}".format(name))
            user = User(username=username, email=email, role=role)
            db.session.add(user)
        db.session.commit()


def init_players():
    players = Player.query.all()
    if players is None or len(players) == 0:
        print("Adding all players")
        for name, username, email, role in _PLAYERS_:
            print("Adding player {}".format(name))
            user = User.query.filter_by(username=username).first()
            if user is None:
                raise Exception('User not found in user table with username "{}"'.format(username))
            hdcp_front = _HANDICAPS_[name][0]
            hdcp_back = _HANDICAPS_[name][1]
            hdcp_total = hdcp_front + hdcp_back
            hdcp_index_nine = str(_HANDICAP_INDICES_NINE_HOLES_[name])
            player = Player(name=name, user_id=user.id, hdcp_front=hdcp_front, hdcp_back=hdcp_back, hdcp_total=hdcp_total,
                            hdcp_index_nine=hdcp_index_nine)
            db.session.add(player)
        db.session.commit()


def init_teams():
    teams = Team.query.all()
    if teams is None or len(teams) == 0:
        print("Adding all teams")
        for name, players in _TEAMS_.items():
            print("Adding team {}".format(name))
            p1 = Player.query.filter_by(name=players[0]).first()
            p2 = Player.query.filter_by(name=players[1]).first()
            team = Team(name=name, player_one=p1.id, player_two=p2.id)
            db.session.add(team)
            print("p1 {} - team {}".format(p1, p1.team_id))
            # commit to DB so we get an id from the entry
            db.session.commit()
            p1.team_id = team.id
            p2.team_id = team.id
            print("p1 {} - team {}".format(p1, p1.team_id))
            # db.session.commit()


def init_defaults():
    """Pre-Populate Tables"""
    init_users()
    init_players()
    init_teams()
