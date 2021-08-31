from flask_table import Col

from app import db
from app.models import Player, Team
from app.tables import PlayerScore, PlayerScoreTable, TeamNetScore, TeamNetTable, TeamBestGrossScore, TeamBestGrossTable


def save_player(player, db_player, modified_holes):
    # Walk through front 9 and back 9. Save gross and net scores.

    front_nine_score = 0
    for i in range(1, 9):
        hole_num = 'hole{}'.format(i)
        if hole_num in modified_holes:
            hole_score = getattr(player, hole_num).data
            setattr(db_player, hole_num, hole_score)
        else:
            hole_score = getattr(db_player, hole_num)
        if hole_score is not None:
            front_nine_score += hole_score
    db_player.front_score = front_nine_score
    db_player.front_net_score = front_nine_score - db_player.hdcp_front

    back_nine_score = 0
    for i in range(10, 19):
        hole_num = 'hole{}'.format(i)
        if hole_num in modified_holes:
            hole_score = getattr(player, hole_num).data
            setattr(db_player, hole_num, hole_score)
        else:
            hole_score = getattr(db_player, hole_num)
        if hole_score is not None:
            back_nine_score += hole_score
    db_player.back_score = back_nine_score
    db_player.back_net_score = back_nine_score - db_player.hdcp_back
    db_player.total_score = front_nine_score + back_nine_score
    db_player.total_net_score = front_nine_score + back_nine_score - db_player.hdcp_total


def save_players(league):

    modified = league.modified.data.strip()
    modified_players_holes = {}  # { name: [holes] }
    if not modified:
        print('No scores modified.. Won\'t process new scores')
        return

    # Build a map of name to list of holes. Only store/save the modified holes on this form submission
    modified = modified.split('; ')
    modified = [m.split('-') for m in modified]
    for m in modified:
        name = m[0]
        hole = m[1]
        if name in modified_players_holes.keys():
            modified_players_holes[name].append(hole)
        else:
            modified_players_holes[name] = [hole]

    print('MODIFIED player_holes {}'.format(modified_players_holes))

    for player in league.players:
        player_name = player.player_name.data
        if player_name not in modified_players_holes.keys():
            continue

        db_player = Player.query.filter_by(name=player_name).first()
        print("Saving player {}; dbplayer {}".format(player_name, db_player))
        save_player(player, db_player, modified_players_holes[player_name])
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

    front_scores = sorted(front_scores, key=lambda score: score.net_score if score and score.net_score else 0)
    back_scores = sorted(back_scores, key=lambda score: score.net_score if score and score.net_score else 0)
    total_scores = sorted(total_scores, key=lambda score: score.net_score if score and score.net_score else 0)
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


def create_team_best_gross_table():
    team_gross_scores = []
    for i in range(1, 6):
        teams = Team.query.filter_by(foursome=i).all()
        if len(teams) != 2:
            raise Exception('Can\'t find teams for foursome #{}'.format(i))
        team1 = teams[0]
        team2 = teams[1]
        p1 = Player.query.get(team1.player_one)
        p2 = Player.query.get(team1.player_two)
        p3 = Player.query.get(team2.player_one)
        p4 = Player.query.get(team2.player_two)

        score_table_obj = TeamBestGrossScore('{} - {}'.format(team1.name, team2.name))
        total_score = 0
        for h in range(1, 19):
            hole = 'hole{}'.format(h)
            # get hole score for all 4 players, sort it, and take the first 3.
            top_scores = sorted([getattr(player, hole) for player in [p1, p2, p3, p4]], key=lambda x: (x is None, x))[:3]
            total = sum(filter(None, top_scores))
            setattr(score_table_obj, hole, total)
            total_score += total

        setattr(score_table_obj, 'score', total_score)
        team_gross_scores.append(score_table_obj)

    team_gross_scores = sorted(team_gross_scores, key=lambda score: score.score)
    table = TeamBestGrossTable(team_gross_scores, table_id='best-gross')
    for h in range(1, 19):
        hole_ = 'hole{}'.format(h)
        hole = 'Hole {}'.format(h)
        table.add_column(hole_, Col(hole, td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'}))
    table.add_column('score', Col('Score', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'}))
    return table


def create_scoring_tables():
    players = Player.query.all()
    front_table, back_table, total_table = create_player_tables(players)
    team_table = create_team_table(players)
    team_best_gross_table = create_team_best_gross_table()
    return front_table, back_table, total_table, team_table, team_best_gross_table
