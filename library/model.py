from dao import User, Question, Answer
from . import db

def insert_to_db(dao_object):
    db.session.add(dao_object)
    db.session.commit()

def remove_from_db(dao_object):
    db.session.delete(dao_object)
    db.session.commit()