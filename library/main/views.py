from flask import render_template, redirect, url_for, flash, request
from flask.ext.login import login_required, current_user
from . import main
from ..dao import User, Question, Answer
from ..model import insert_to_db
from .forms import AddQuestionForm, AddAnswerForm


@main.route('/')
def index_html():
    #current_app.logger.error('An error occurred')
   return redirect(url_for('auth.login'))

@main.route('/show_questions', methods=['GET', 'POST'])
@login_required
def show_questions():
    questions = Question.query.all()
    form = AddQuestionForm()
    if form.validate_on_submit():
        question = Question(questionname = form.questionname.data)
        question.question_partisipants.append(current_user)
        print question.question_partisipants
        insert_to_db(question)
        flash('The question has been updated.')
        return redirect(url_for('main.show_questions',username = current_user.username))
    return render_template('questions.html', questions = questions, current_user = current_user, form = form)

@main.route('/question/<int:id>', methods=['GET', 'POST'])
@login_required
def show_question(id):
    question = Question.query.filter_by(id = id).first()
    if current_user not in question.question_partisipants:
        question.question_partisipants.append(current_user)
    answers = Answer.query.filter_by(questionid=id).order_by('timestamp')
    form  = AddAnswerForm()
    if form.validate_on_submit():
        answer = Answer(text = form.text.data, userid = current_user.id, questionid = id)
        insert_to_db(answer)
        flash('The answer has been updated.')
        return redirect(url_for('main.show_question',id = id))
    return render_template('question.html', answers = answers, current_user = current_user, form = form)


@main.route('/search_for_question/', methods=['POST'])
@login_required
def search_for_question():
    search_text = request.form['search_text']
    questions = Question.query.filter(Question.questionname.like("%"+search_text+"%")).all()
    form = AddQuestionForm()
    return render_template('questions.html', questions = questions, current_user = current_user, form = form)

