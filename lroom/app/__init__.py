from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import settings
from flask_assets import Environment, Bundle


app = Flask(__name__)
assets = Environment(app)
basedir = settings.BASE_DIR
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB
app.secret_key = settings.SECRET_KEY
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
Bootstrap(app)
from app import models, views
js = Bundle('js/jquery-3.2.1.min.js', 'js/bootstrap.js', 'js/main.js', filters='jsmin', output='gen/script.js')
assets.register('script', js)
css = Bundle('css/bootstrap.css', 'css/main.css', filters='cssmin', output='gen/style.css')
assets.register('style', css)
