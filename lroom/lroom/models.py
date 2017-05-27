from sqlalchemy import Column, Integer, String, Text

from lroom.database import Base


class Page(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    slug = Column(String(200), unique=True)
    text = Column(Text)

    def __init__(self, title, slug, text):
        self.title = title
        self.slug = slug
        self.text = text

    def __unicode__(self):
        return self.title
