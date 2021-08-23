import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'abcd1234'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'scores.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
