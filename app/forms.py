from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FieldList, FormField, TextAreaField
from wtforms.validators import DataRequired, Optional


# class Hole(FlaskForm):
#     holenum = IntegerField('number', default=5)
#     number = TextAreaField()
#     # number = IntegerField()


class PlayerScoreForm(FlaskForm):
    player_name = StringField('name', render_kw={'readonly': True})
    # holes = FieldList(FormField(Hole))
    hole1 = IntegerField('1', validators=[Optional()])
    hole2 = IntegerField('2', validators=[Optional()])
    hole3 = IntegerField('3', validators=[Optional()])
    hole4 = IntegerField('4', validators=[Optional()])
    hole5 = IntegerField('5', validators=[Optional()])
    hole6 = IntegerField('6', validators=[Optional()])
    hole7 = IntegerField('7', validators=[Optional()])
    hole8 = IntegerField('8', validators=[Optional()])
    hole9 = IntegerField('9', validators=[Optional()])
    hole10 = IntegerField('10', validators=[Optional()])
    hole11 = IntegerField('11', validators=[Optional()])
    hole12 = IntegerField('12', validators=[Optional()])
    hole13 = IntegerField('13', validators=[Optional()])
    hole14 = IntegerField('14', validators=[Optional()])
    hole15 = IntegerField('15', validators=[Optional()])
    hole16 = IntegerField('16', validators=[Optional()])
    hole17 = IntegerField('17', validators=[Optional()])
    hole18 = IntegerField('18', validators=[Optional()])


class LeagueForm(FlaskForm):
    title = StringField('title')
    players = FieldList(FormField(PlayerScoreForm))
    submit = SubmitField('Submit Scores', render_kw={'onclick': 'loading();'})
