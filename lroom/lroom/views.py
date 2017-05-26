from lroom import app
from models import Page


@app.route('/')
def index():
    return 'Hello World!'
