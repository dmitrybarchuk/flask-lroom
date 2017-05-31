from app import db


class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), )
    slug = db.Column(db.String(200), unique=True)
    text = db.Column(db.Text, nullable=True)
    published = db.Column(db.Boolean, default=True)

    def __init__(self, title, slug, text, published):
        self.title = title
        self.slug = slug
        self.text = text
        self.published = published

    def __unicode__(self):
        return self.title
