import os

DEBUG = False
basedir = os.path.abspath(os.path.dirname(__file__))

db = 'sqlite:///' + os.path.join(basedir, 'lroom.sqlite')

import local_settings
