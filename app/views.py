from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
def base():
    return "this is root"
    
@app.route('/index')
def index():
    user = {'nickname': 'user1'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
    
    
    
    
@app.route('/testroute')
def testman():
    return "hit test route"