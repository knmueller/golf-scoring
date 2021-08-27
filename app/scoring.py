from app import db
from app.models import Player, Team
from app.tables import PlayerScore, PlayerScoreTable, TeamNetScore, TeamNetTable


def save_player(player, db_player):
    # Walk through front 9 and back 9. Save gross and net scores.

    front_nine_score = 0
    for i in range(1, 9):
        hole_num = 'hole{}'.format(i)
        hole_score = getattr(player, hole_num).data
        setattr(db_player, hole_num, hole_score)
        if hole_score is not None:
            front_nine_score += hole_score
    db_player.front_score = front_nine_score
    db_player.front_net_score = front_nine_score - db_player.hdcp_front

    back_nine_score = 0
    for i in range(10, 19):
        hole_num = 'hole{}'.format(i)
        print('checking {}'.format(hole_num))
        hole_score = getattr(player, hole_num).data
        setattr(db_player, hole_num, hole_score)
        if hole_score is not None:
            back_nine_score += hole_score
    db_player.back_score = back_nine_score
    db_player.back_net_score = back_nine_score - db_player.hdcp_back
    db_player.total_score = front_nine_score + back_nine_score
    db_player.total_net_score = front_nine_score + back_nine_score - db_player.hdcp_total


def save_players(league):
    for player in league.players:
        player_name = player.player_name.data
        db_player = Player.query.filter_by(name=player_name).first()
        save_player(player, db_player)
    db.session.commit()


def create_player_tables(players):
    front_scores = []
    back_scores = []
    total_scores = []
    for player in players:
        display_name = '{} ({})'.format(player.name, player.hdcp_total)
        front_scores.append(PlayerScore(display_name, player.front_score, player.front_net_score))
        back_scores.append(PlayerScore(display_name, player.back_score, player.back_net_score))
        total_scores.append(PlayerScore(display_name, player.total_score, player.total_net_score))

    # TODO BUGBUG here where sorted crashes after a clean, initialized DB if going straight to Results screen
    #      without hitting Submit once on entering scores.
    front_scores = sorted(front_scores, key=lambda score: score.net_score)
    back_scores = sorted(back_scores, key=lambda score: score.net_score)
    total_scores = sorted(total_scores, key=lambda score: score.net_score)
    return PlayerScoreTable(front_scores, table_id='front-nine'), \
           PlayerScoreTable(back_scores, table_id='back-nine'), \
           PlayerScoreTable(total_scores, table_id='total-net')


def create_team_table(players):
    teams = Team.query.all()
    team_scores = []
    for team in teams:
        # player id is 1 based where the player list is 0 based, so -1 on the index for the correct player
        player_one = players[team.player_one - 1]
        player_two = players[team.player_two - 1]
        table_name = '{} ({}, {})'.format(team.name, player_one.name, player_two.name)
        team_scores.append(TeamNetScore(table_name, player_one.total_net_score, player_two.total_net_score))

    team_scores = sorted(team_scores, key=lambda score: score.net_score)
    return TeamNetTable(team_scores, table_id='team-net')


def create_scoring_tables():
    players = Player.query.all()
    front_table, back_table, total_table = create_player_tables(players)
    team_table = create_team_table(players)
    return front_table, back_table, total_table, team_table
