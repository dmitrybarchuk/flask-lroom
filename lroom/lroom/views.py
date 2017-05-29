from flask import render_template, redirect, flash, request, url_for
from lroom import app
from lroom.database import db_session
from models import Page


@app.route('/')
def index():
    return render_template('base.html', page=u'Hello, World!')


@app.route('/<page_slug>')
def page(page_slug):
    page_content = Page.query.filter_by(slug=page_slug).first()
    return render_template('page.html', **{
                           'page': page_content if page_content else page_slug,
                           'title': page_content.title if page_content else page_slug,
                           })


@app.route('/<page_slug>/edit/', methods=['POST', 'GET'])
def page_edit(page_slug):
    flash('New entry was successfully posted')
    return render_template('edit.html', page='')


@app.route('/edit', methods=['POST'])
def edit_page():
    form = Page(request.form['title'], request.form['slug'], request.form['text'])
    db_session.add(form)
    db_session.commit()
    flash('Entry was successfully changed')
    return redirect(url_for('page'))
