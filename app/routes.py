from flask import render_template, request, send_file, flash, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import redirect

from app import app, db
from app.forms import LeagueForm, LoginForm, PlayerScoreForm, RegistrationForm, ResetPasswordForm, ResetScoresForm
from app.models import Player, User, Team
from app.scoring import save_players, create_scoring_tables, reset_all_scores

INIT = False


def add_hole(num, form, player):
    hole_score = getattr(player, 'hole{}'.format(num))
    setattr(form, 'hole{}'.format(num), hole_score)


@app.route('/login', methods=['GET', 'POST'])
def login():

    global INIT
    if not INIT:
        # This was in @app.before_first_request (see app/__init__.py). This may be a potential solution instead
        # https://stackoverflow.com/a/74629704
        db.create_all()
        from app.models import init_defaults
        init_defaults()
        # create_tables()
        INIT = True

    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.lower()).first()
        if user is None or not user.check_password(form.password.data):
            if user and user.password_hash is None:
                flash('No password set for this user. Please register.')
            else:
                flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = '/'
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    form = RegistrationForm()
    if form.validate_on_submit():
        # TODO if password already exists for user, fail out. implement reset password
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('User not found to set password')
            return redirect(url_for('register'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your password has been set')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route("/reset_pw", methods=['GET', 'POST'])
@login_required
def reset_pw():
    form = None
    if current_user.role == 'admin':
        form = ResetPasswordForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None:
                flash('User not found to reset password')
                return redirect(url_for('reset_pw'))
            user.set_password(None)
            db.session.commit()
            flash('{}\'s password has been reset. Please re-register'.format(user.username))
            return redirect(url_for('register'))

    return render_template('reset_password.html', form=form)


@app.route("/reset_scores", methods=['GET', 'POST'])
@login_required
def reset_scores():
    form = None
    if current_user.role == 'admin':
        form = ResetScoresForm()
        if form.validate_on_submit():
            reset_all_scores()
            flash('All scores reset')
            return redirect(url_for('reset_scores'))

    return render_template('reset_scores.html', form=form)


@app.route("/help")
def help_page():
    return render_template('help.html')


@app.route('/', methods=['GET', 'POST'])
@login_required
def root():
    print("start /")
    league = LeagueForm()
    if league.validate_on_submit():
        print('submitting scores...')
        save_players(league)
        return redirect('/scoring')

    if request.method == 'GET':
        print("league player length = {}".format(len(league.players)))
        if current_user.role == 'admin':
            players = Player.query.all()
        else:
            # Get all players in the current users foursome
            this_player = Player.query.filter_by(user_id=current_user.id).first()
            player_team = Team.query.get(this_player.team_id)
            foursome = player_team.foursome
            teams = Team.query.filter_by(foursome=foursome).all()
            team_ids = []
            for team in teams:
                team_ids.append(team.id)

            players = Player.query.filter(Player.team_id.in_(team_ids)).all()

        for player in players:
            print('adding player to form {}'.format(player))
            form = PlayerScoreForm()
            form.player_name = f'{player.name} ({player.hdcp_front}, {player.hdcp_back})'
            for i in range(1, 19):
                add_hole(i, form, player)
            league.players.append_entry(form)

    return render_template('enter_scores.html', league=league)


@app.route("/scoring")
@login_required
def calc():
    front_table, back_table, total_table, team_table, team_best_gross_table, champ_match_table = create_scoring_tables()
    return render_template('display_scores.html', front=front_table, back=back_table, total=total_table,
                           team=team_table, best_gross=team_best_gross_table, champ_match_table=champ_match_table)


@app.route("/static/loadingimage.gif")
def loading():
    return send_file('static/loadingimage.gif', mimetype='image/gif')
