import unittest
from flask import current_app, url_for
from library import create_app, db
from library.dao import User

class DAOTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_useradd_noemail(self):
        user = User(username="test12",
                    password="test1234")
        db.session.add(user)
        #This must be broken!!!! Used for "must have errors" searching
        with self.assertRaises(Exception) as context:
            db.session.commit()
        self.assertTrue(context.exception)
        
        
    def test_useradd_everything_fine(self):
        user = User(username="test12",
                    email = "123@123.ua",
                    password="test1234")
        db.session.add(user)
        self.assertTrue(db.session.commit() is not False)