import os


SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname('app.py'))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/rh_chat'

SQLALCHEMY_TRACK_MODIFICATIONS = False
