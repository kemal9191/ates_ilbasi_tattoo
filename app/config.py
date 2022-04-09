import os


class Config:
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/tattoo'
