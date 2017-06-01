from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form
from app.models import Page

PageForm = model_form(Page, FlaskForm)
