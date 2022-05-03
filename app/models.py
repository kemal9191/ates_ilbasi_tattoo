from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import ARRAY


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    seo_statement = db.Column(db.String())
    seo_keywords = db.Column(db.String())
    image = db.Column(db.String(), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

    def __repr__(self):
        return f"Content {self.name} has been uploaded"


'''class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Post {self.title} has been uploaded"'''
@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(admin_id)


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    Contents = db.relationship('Content', backref='admin', lazy=True)


class FormRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_surname = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), nullable=False)
    subject = db.Column(db.String(), nullable=False)
    message = db.Column(db.String(), nullable=False)
    images = db.Column(ARRAY(db.String()))
    date = db.Column(db.DateTime(), default=datetime.utcnow)
