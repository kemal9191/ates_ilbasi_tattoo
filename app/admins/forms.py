from ast import In
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = CKEditorField('Content')
    image = FileField('Upload a post picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save')


class TattooForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    image = FileField('Upload a tattoo picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')
