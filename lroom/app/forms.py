# coding:utf-8
from wtforms import Form, BooleanField, StringField, validators, TextAreaField, SubmitField


class PageForm(Form):
    title = StringField(u'Заголовок страницы', [validators.InputRequired(message=u'Поле обязательно для заполнения'), validators.Length(max=200)])
    slug = StringField(u'slug', [validators.InputRequired(message=u'Поле обязательно для заполнения'), validators.Length(max=200)])
    text = TextAreaField(u'Содержимое страницы')
    published = BooleanField(u'Опубликовано')
