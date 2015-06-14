from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError


class AddQuestionForm(Form):
    questionname = PageDownField("", validators=[Required()])
    submit = SubmitField('Add')


class AddAnswerForm(Form):
    text = PageDownField("", validators=[Required()])
    submit = SubmitField('Answer')
