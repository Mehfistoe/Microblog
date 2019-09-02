from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'McKenzie'}
    posts = [
        {
            'author': {'username': 'Sarah'},
            'body': 'Updates to Copper, Spidey.'
        },
        {
            'author': {'username':'Harvey'},
            'body': 'Armstrong sucks.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

