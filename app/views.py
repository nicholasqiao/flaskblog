from app import app
from flask import render_template

@app.route('/')
def base():
    return "this is root"
    
@app.route('/index')
def index():
    user = {'nickname': 'user1'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
    
@app.route('/testroute')
def testman():
    return "hit test route"