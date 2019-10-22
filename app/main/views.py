from flask import render_template,request,redirect,url_for,abort
from . import main
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    View root page function that returns the signup page and its data
    '''
    if request.method == 'POST':
        username = request.form.get('username').strip()
        email = request.form.get('email').strip()
        password = request.form.get('password').strip()

        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('signup.html', error=f'User with email {email} already exists')
        new_user = User(username=username, email=email, password_hash=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('signup.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').strip()
        password = request.form.get('password').strip()

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return render_template('login.html', error="Invalid credentials")
        return redirect(url_for('main.index'))
    return render_template('login.html')


    


