# QUESTION: what does an __init__ file do
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__) # initializes/defines the Flask app
app.config.from_object(Config) # initializes config values
db = SQLAlchemy(app) # initializes the DB
# Migrate handles updates to the DB that happen in the app
migrate = Migrate(app, db) # initializes the Migration service

# LoginManager allows users to login to an app 
login = LoginManager(app)
# 'login' is the endpoint name for the login view
login.login_view = 'login'

from app import routes, models

