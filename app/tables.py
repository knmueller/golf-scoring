from flask_table import Table, Col


# used for front, back, total
class PlayerScoreTable(Table):
    # allow_sort = True  ## look up examples for sort https://flask-table.readthedocs.io/en/stable/
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
    # allow_sort = True  ## look up examples for sort https://flask-table.readthedocs.io/en/stable/
    classes = ['scoring_table']
    name = Col('Name')  # team name
    player_one_net = Col('Player 1 Net', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})
    player_two_net = Col('Player 2 Net', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})
    net_score = Col('Net Score', td_html_attrs={'class': 'table__cell'}, th_html_attrs={'class': 'table__cell'})

    def get_thead_attrs(self):
        return {'class': 'table__header'}

    def get_tr_attrs(self, item):
        return {'class': 'table__row'}


class TeamNetScore(NetScore):
    def __init__(self, name, player_one_net, player_two_net):
        NetScore.__init__(self, name, player_one_net + player_two_net)
        self.player_one_net = player_one_net
        self.player_two_net = player_two_net
