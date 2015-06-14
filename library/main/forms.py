from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Length


class AddQuestionForm(Form):
    questionname = StringField('Question Title', validators=[Required(), Length(1, 128)])
    questiontext = TextAreaField('Question Body', validators=[Required(), Length(1, 999)])
    submit = SubmitField('Add Question')


class AddAnswerForm(Form):
    text = StringField('Your Answer', validators=[Required(), Length(1, 999)])
    submit = SubmitField('Answer')
