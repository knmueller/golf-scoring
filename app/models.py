from app import db
from initial_data import _HANDICAPS_, _HANDICAP_INDICES_NINE_HOLES_, _PLAYERS_, _TEAMS_


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
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


def init_players():
    players = Player.query.all()
    print("players = {}".format(players))
    if players is None or len(players) == 0:
        print("Adding all players")
        for name in _PLAYERS_:
            print("Adding player {}".format(name))
            hdcp_front = _HANDICAPS_[name][0]
            hdcp_back = _HANDICAPS_[name][1]
            hdcp_total = hdcp_front + hdcp_back
            hdcp_index_nine = str(_HANDICAP_INDICES_NINE_HOLES_[name])
            player = Player(name=name, hdcp_front=hdcp_front, hdcp_back=hdcp_back, hdcp_total=hdcp_total,
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
            print("dir p1 {}".format(dir(p1)))
            p1.team_id = team.id
            p2.team_id = team.id
            db.session.commit()


def init_defaults():
    """Pre-Populate Tables"""
    init_players()
    init_teams()
