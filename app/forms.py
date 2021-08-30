from app.models import User

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FieldList, FormField, PasswordField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Optional, ValidationError, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('Username does not exist.')


class ResetPasswordForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Reset')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('Username does not exist.')


class PlayerScoreForm(FlaskForm):
    player_name = StringField('name', render_kw={'readonly': True})
    hole1 = IntegerField('1', validators=[Optional()], render_kw={'type': 'number'})
    hole2 = IntegerField('2', validators=[Optional()], render_kw={'type': 'number'})
    hole3 = IntegerField('3', validators=[Optional()], render_kw={'type': 'number'})
    hole4 = IntegerField('4', validators=[Optional()], render_kw={'type': 'number'})
    hole5 = IntegerField('5', validators=[Optional()], render_kw={'type': 'number'})
    hole6 = IntegerField('6', validators=[Optional()], render_kw={'type': 'number'})
    hole7 = IntegerField('7', validators=[Optional()], render_kw={'type': 'number'})
    hole8 = IntegerField('8', validators=[Optional()], render_kw={'type': 'number'})
    hole9 = IntegerField('9', validators=[Optional()], render_kw={'type': 'number'})
    hole10 = IntegerField('10', validators=[Optional()], render_kw={'type': 'number'})
    hole11 = IntegerField('11', validators=[Optional()], render_kw={'type': 'number'})
    hole12 = IntegerField('12', validators=[Optional()], render_kw={'type': 'number'})
    hole13 = IntegerField('13', validators=[Optional()], render_kw={'type': 'number'})
    hole14 = IntegerField('14', validators=[Optional()], render_kw={'type': 'number'})
    hole15 = IntegerField('15', validators=[Optional()], render_kw={'type': 'number'})
    hole16 = IntegerField('16', validators=[Optional()], render_kw={'type': 'number'})
    hole17 = IntegerField('17', validators=[Optional()], render_kw={'type': 'number'})
    hole18 = IntegerField('18', validators=[Optional()], render_kw={'type': 'number'})


class LeagueForm(FlaskForm):
    title = StringField('title')
    players = FieldList(FormField(PlayerScoreForm))
    submit = SubmitField('Submit Scores', render_kw={'onclick': 'loading(); getChangedFields();'})
    modified = HiddenField("modified_scores")
