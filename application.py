#!/usr/bin/env python
import os
from library import create_app

application = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    application.debug = True
    application.run()
