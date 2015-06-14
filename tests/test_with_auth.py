import unittest
from flask import current_app, url_for
from library import create_app, db
from library.dao import User, Chat
import re

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
        db.create_all()
        user1 = User(email="test1@123.ua",
                    username="test1",
                    password="test1234")
        chat1 = Chat(chatname="test123")
        user2 = User(email="test2@123.ua",
                    username="test2",
                    password="test1234")
        chat2 = Chat(chatname="test12")
        db.session.add(chat1)
        db.session.add(chat2)
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
    
    def test_bed_auth(self):
        response = self.client.post(url_for('auth.login'), data={
        'email': 'test1@123.ua',
        'password': 'lalala'
        }, follow_redirects=True)
        self.assertTrue(re.search(b'Login', response.data))
        
    def test_good_auth(self):
        response = self.client.post(url_for('auth.login'), data={
        'email': 'test1@123.ua',
        'password': 'test1234'
        }, follow_redirects=True)
        self.assertTrue(re.search(b'test1', response.data))