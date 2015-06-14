from flask import render_template, redirect, url_for, flash, request
from flask.ext.login import login_required, current_user
from . import main
from ..dao import Question, Answer
from ..model import insert_to_db
from .forms import AddQuestionForm, AddAnswerForm


@main.route('/')
def index_html():
    # current_app.logger.error('An error occurred')
    return redirect(url_for('main.show_questions'))


@main.route('/show_questions', methods=['GET', 'POST'])
def show_questions():
    questions = Question.query.all()
    form = AddQuestionForm()
    if form.validate_on_submit():
        question = Question(questionname=form.questionname.data, text=form.questiontext.data,
                            author=current_user._get_current_object())
        insert_to_db(question)
        flash('The question has been added.')
        return redirect(url_for('main.show_questions'))
    return render_template('questions.html', questions=questions, current_user=current_user, form=form)


@main.route('/question/<int:id>', methods=['GET', 'POST'])
def show_question(id):
    question = Question.query.filter_by(id=id).first()
    answers = Answer.query.filter_by(questionid=id).order_by('timestamp').all()
    form = AddAnswerForm()
    if form.validate_on_submit():
        answer = Answer(text=form.text.data, question=question, author=current_user._get_current_object())
        insert_to_db(answer)
        flash('The answer has been added.')
        return redirect(url_for('main.show_question', id=id))
    return render_template('question.html', answers=answers, current_user=current_user, form=form,
                           question=question)


@main.route('/search_for_question/', methods=['POST'])
@login_required
def search_for_question():
    search_text = request.form['search_text']
    questions = Question.query.filter(Question.text.like("%" + search_text + "%")).all()
    form = AddQuestionForm()
    return render_template('questions.html', questions=questions, current_user=current_user, form=form)


# TODO Make POST here!!!
@main.route('/like/<int:id>', methods=['GET'])
@login_required
def like_answer(id):
    answer = Answer.query.filter_by(id=id).first()
    print answer.likes
    if current_user not in answer.likes:
        try:
            answer.likes.append(current_user._get_current_object())
        except NoneType as detail:
            print 'No Object current user', detail
    return redirect(url_for('main.show_question', id=answer.questionid))
