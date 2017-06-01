# coding:utf-8
from flask import render_template, request

from app import app
from app.models import Page


@app.route('/')
def index():
    return render_template('base.html', text=u'Привет')


@app.route('/<page_slug>')
def page(page_slug):
    return render_template('page.html', page=Page.query.filter_by(slug=page_slug, published=True).first())


@app.route('/<page_slug>/edit/', methods=['GET', 'POST'])
def page_edit(page_slug):
    page = Page.query.filter_by(slug=page_slug).first()
    if page:
        return render_template('page_form.html', page=page)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
