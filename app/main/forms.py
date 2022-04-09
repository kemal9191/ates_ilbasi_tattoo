from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name*', validators=[DataRequired()])
    email = StringField('Email*', validators=[DataRequired(), Email()])
    subject = StringField('Subject*', validators=[DataRequired()])
    message = TextAreaField('Message*', validators=[DataRequired()])
    submit = SubmitField('GÖNDER')

