# coding:utf-8
from flask import render_template, request, flash, redirect, url_for
from forms import PageForm
from app import app, db
from app.models import Page


@app.route('/')
def index():
    return render_template('base.html', page=u'Привет', menu=Page.query.filter_by(published=True))


@app.route('/<page_slug>')
def page(page_slug):
    menu = Page.query.filter_by(published=True)
    return render_template('page.html', menu=menu, page=menu.filter_by(slug=page_slug).first())


@app.route('/admin')
def admin():
    return render_template('admin.html', pages=Page.query.all())


@app.route('/admin/page/<page_id>/', methods=['GET', 'POST'])
def page_edit(page_id):
    if page_id != 'create':
        item = Page.query.filter_by(id=page_id).first()
    else:
        item = Page()

    form = PageForm(request.form, item)

    if request.method == 'POST' and form.validate():
        form.populate_obj(item)
        item.save()

        flash(u'Страница %s сохранена' % form.title.data)
        return redirect(url_for('admin'))
    else:
        return render_template('page_form.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
