#!/usr/bin/env python
import os
from library import create_app, db
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

treschat = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(treschat)
migrate = Migrate(treschat, db)

manager.add_command("runserver", Server(host="0.0.0.0", port=8080))


def make_shell_context():
    return dict(treschat=treschat, db=db)
    
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test(coverage=False):
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
    