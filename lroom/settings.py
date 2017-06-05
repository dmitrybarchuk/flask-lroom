import os

DEBUG = False
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB = 'sqlite:///' + os.path.join(BASE_DIR, 'lroom.sqlite')
SECRET_KEY = 'GHFhVGcgfcTR^%rT678tUY7ftVFhgch'
WTF_CSRF_ENABLED = True

try:
    from local_settings import *
except:
    pass
