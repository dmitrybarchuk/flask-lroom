# coding:utf-8
from flask import render_template, request, flash, redirect, url_for
from forms import PageForm
from app import app, db
from app.models import Page


@app.route('/')
def index():
    return render_template('base.html', text=u'Привет')


@app.route('/<page_slug>')
def page(page_slug):
    return render_template('page.html', page=Page.query.filter_by(slug=page_slug, published=True).first())


@app.route('/<page_slug>/edit/', methods=['GET', 'POST'])
def page_edit(page_slug):
    item = Page.query.filter_by(slug=page_slug).first()
    form = PageForm(request.form, item)

    if request.method == 'POST' and form.validate():
        # todo: validation of form
        form.populate_obj(request.form)
        db.session.commit()
        flash(u'Страница %s сохранена' % form.title.data)
        return redirect(url_for('page', page_slug=page_slug))

    return render_template('page_form.html', form=form, page=item)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
