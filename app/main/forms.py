from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = TextAreaField('Content', validators=[InputRequired()])
    submit = SubmitField('Send')

