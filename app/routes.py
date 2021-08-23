from flask import render_template, request, send_file
from werkzeug.utils import redirect

from app import app
from app.forms import LeagueForm, PlayerScoreForm
from app.models import Player
from app.scoring import save_players, create_scoring_tables


def add_hole(num, form, player):
    hole_score = getattr(player, 'hole{}'.format(num))
    setattr(form, 'hole{}'.format(num), hole_score)
    # hole_field = vars(form)['_fields']['hole{}'.format(num)]
    # hole_field.id = '{}-hole{}'.format(player.name, num)
    # hole_field.name = '{}-hole{}'.format(player.name, num)
    # hole_field.short_name = '{}-hole{}'.format(player.name, num)
    # hole_field.label = '{}-hole{}'.format(player.name, num)
    # vars(form)['_fields']['hole{}'.format(num)] = hole_field
    # if player.name == "Mueller, Kyle":
    #     print("hole_field {}".format(vars(hole_field)))
    #     print(holeattr)
    #     print()


@app.route('/', methods=['GET', 'POST'])
def root():
    print("start /")
    league = LeagueForm()
    if league.validate_on_submit():
        # flash('Submitting scores...')
        print('submitting scores...')
        save_players(league)
        return redirect('/scoring')

    if request.method == 'GET':
        print("league player length = {}".format(len(league.players)))
        players = Player.query.all()
        for player in players:
            form = PlayerScoreForm()
            form.player_name = str(player.name)
            for i in range(1, 19):
                add_hole(i, form, player)
            league.players.append_entry(form)

    return render_template('enter_scores.html', league=league)


@app.route("/scoring")
def calc():
    print("TODO display scoring")
    front_table, back_table, total_table, team_table = create_scoring_tables()
    return render_template('display_scores.html', front=front_table, back=back_table, total=total_table,
                           team=team_table)


@app.route("/static/loadingimage.gif")
def loading():
    return send_file('static/loadingimage.gif', mimetype='image/gif')
