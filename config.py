import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-if-not-set')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shortener.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False