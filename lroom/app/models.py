# coding:utf-8
from app import db


class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), )
    slug = db.Column(db.String(200), unique=True)
    text = db.Column(db.Text, nullable=True)
    published = db.Column(db.Boolean, default=True)

    def __unicode__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()


class Gallery(db.Model):
    __tablename__ = 'galleries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    slug = db.Column(db.String(200), unique=True)
    images = db.Column(db.Text)
    published = db.Column(db.Boolean, default=True)

    def __unicode__(self):
        return self.title
