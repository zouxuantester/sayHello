import os

from sayhello import app

SECRET_KEY = os.getenv('SECRET_KEY', 'mytest')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')