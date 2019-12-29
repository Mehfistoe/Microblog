import os
# says to work in the directory this Python file is in
basedir = os.path.abspath(os.path.dirname(__file__))

# This class holds all of the configuration settings for the Flask app
class Config(object):
    # QUESTION: where does os.environ look to get it's values
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATEBASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    # QUESTION: what is this
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['macnchez.r@gmail.com']

