# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField


class UploadForm(FlaskForm):
    description = TextAreaField('Description')
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg','jpeg', 'png'], 'Images only!')
    ])