from flask_table import Table, Col


# used for front, back, total
class PlayerScoreTable(Table):
    classes = ['scoring_table', 'inline_table']
    name = Col('Name', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})  # player name
    gross_score = Col('Gross Score', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})
    net_score = Col('Net Score', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})

    def get_thead_attrs(self):
        return {'class': 'table__header'}

    def get_tr_attrs(self, item):
        return {'class': 'table__row'}


class NetScore(object):
    def __init__(self, name, net_score):
        self.name = name
        self.net_score = net_score


class PlayerScore(NetScore):
    def __init__(self, name, gross_score, net_score):
        NetScore.__init__(self, name, net_score)
        self.gross_score = gross_score


class TeamNetTable(Table):
    classes = ['scoring_table']
    name = Col('Name', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})  # team name
    player_one_net = Col('Player 1 Net', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})
    player_two_net = Col('Player 2 Net', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})
    net_score = Col('Net Score', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})

    def get_thead_attrs(self):
        return {'class': 'table__header'}

    def get_tr_attrs(self, item):
        return {'class': 'table__row'}


class TeamNetScore(NetScore):
    def __init__(self, name, player_one_net, player_two_net):
        p1_net = player_one_net # if player_one_net is not None else 0
        p2_net = player_two_net # if player_two_net is not None else 0
        NetScore.__init__(self, name, p1_net + p2_net if p1_net and p2_net else None)
        self.player_one_net = p1_net
        self.player_two_net = p2_net

    def __repr__(self):
        return '<TeamTeamNetScore {} ; {} ; {} ; {}>'.format(self.name, self.player_one_net, self.player_two_net, self.net_score)


class TeamBestGrossTable(Table):
    classes = ['scoring_table']
    name = Col('Foursome', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})
    # dynamic columns
        # holes 1 through 18 - (score1, score2, score3) sum
        # score = Col('Score', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})

    def get_thead_attrs(self):
        return {'class': 'table__header'}

    def get_tr_attrs(self, item):
        return {'class': 'table__row'}


class TeamBestGrossScore(object):
    def __init__(self, name):
        self.name = name


class ChampMatchTable(Table):
    classes = ['scoring_table']
    name = Col('Player', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})
    # dynamic columns
        # holes 1 through 18 - (score1, score2, score3) sum

    def get_thead_attrs(self):
        return {'class': 'table__header'}

    def get_tr_attrs(self, item):
        return {'class': 'table__row'}


class ChampMatchScore(object):
    def __init__(self, name):
        self.name = name
