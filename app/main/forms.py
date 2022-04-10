from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('İsim Soyisim*', validators=[DataRequired()])
    email = StringField('E-mail Adresi*', validators=[DataRequired(), Email()])
    subject = StringField('Konu*', validators=[DataRequired()])
    message = TextAreaField('Mesajınız*', validators=[DataRequired()])
    submit = SubmitField('GÖNDER')

