# coding:utf-8
from flask_wtf.file import FileAllowed
from wtforms import Form, BooleanField, StringField, validators, TextAreaField, FileField


class PageForm(Form):
    title = StringField(u'Заголовок страницы', [validators.InputRequired(message=u'Поле обязательно для заполнения'), validators.Length(max=200)])
    slug = StringField(u'slug', [validators.InputRequired(message=u'Поле обязательно для заполнения'), validators.Length(max=200)])
    text = TextAreaField(u'Содержимое страницы')
    published = BooleanField(u'Опубликовано')


class GalleryForm(Form):
    title = StringField(u'Заголовок галереи', [validators.InputRequired(message=u'Поле обязательно для заполнения'),
                                                validators.Length(max=200)])
    slug = StringField(u'slug', [validators.InputRequired(message=u'Поле обязательно для заполнения'),
                                 validators.Length(max=200)])
    image = FileField('image', validators=[FileAllowed(['jpg', 'jpeg', 'png'], u'Только изображения в формате '
                                                                               u'.jpg, .jpeg или .png')])
    published = BooleanField(u'Опубликовано')
