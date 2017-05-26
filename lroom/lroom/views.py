from flask import render_template

from lroom import app
from models import Page


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/<page_slug>')
def page(page_slug):
    return render_template('page.html', page=Page.query.filter_by(slug=page_slug).first())
