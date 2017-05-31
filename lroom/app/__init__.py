from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import settings


app = Flask(__name__)
basedir = settings.basedir
app.config['SQLALCHEMY_DATABASE_URI'] = settings.db
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

from app import models, views
