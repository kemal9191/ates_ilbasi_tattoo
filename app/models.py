from datetime import datetime
from app import db
from sqlalchemy import ForeignKey, DateTime

class Tattoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Tattoo {self.name} has been uploaded"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Post {self.title} has been uploaded"


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Tattoo {self.name} has been uploaded"


class FormRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)
