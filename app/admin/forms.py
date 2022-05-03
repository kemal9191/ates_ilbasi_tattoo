from ast import In
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, DataRequired, Length

'''class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = CKEditorField('Content')
    image = FileField('Upload a post picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save')'''


class ContentForm(FlaskForm):
    name = StringField('BAŞLIK:', validators=[InputRequired()])
    description = TextAreaField('AÇIKLAMA: ')
    seo_statement = StringField('SEO AÇIKLAMASI: ', validators=[DataRequired(), Length(max=320, message='Please shorthen your statement!')])
    seo_keywords = StringField('SEO ANAHTAR KELİMELER: ', validators=[DataRequired()])
    image = FileField('Dövme resmi yükleyin', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('KAYDET')


class LoginForm(FlaskForm):
    username = StringField('KULLANICI ADI:', validators=[DataRequired()])
    password = PasswordField('PAROLA:', validators=[DataRequired()])
    submit = SubmitField('GİRİŞ YAP')
