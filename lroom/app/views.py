# coding:utf-8
from flask import render_template

from app import app
from app.models import Page


@app.route('/')
def index():
    return render_template('base.html', text=u'Привет')


@app.route('/<page_slug>')
def page(page_slug):
    return render_template('page.html', page=Page.query.filter_by(slug=page_slug, published=True).first())
