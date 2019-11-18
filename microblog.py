# QUESTION: what is the difference between app and app
from app import app, db
# app.models reference Python scripts that define DB tables
from app.models import User, Post

# QUESTION: what does this generator do
@app.shell_context_processor
# QUESTION: what is the purpose of this function
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

