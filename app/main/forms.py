from wtforms import StringField, TextAreaField, SubmitField, MultipleFileField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed

class ContactForm(FlaskForm):
    name_surname = StringField('İsim Soyisim*', validators=[DataRequired()])
    email_address = StringField('E-mail Adresi*', validators=[DataRequired(), Email()])
    subject = StringField('Konu*', validators=[DataRequired()])
    message = TextAreaField('Mesajınız*', validators=[DataRequired()])
    images = MultipleFileField('Görsel(ler)inizi yükleyin', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('GÖNDER')

