from os import environ, path
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy()
login_manager = LoginManager()



   
