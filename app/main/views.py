from flask import render_template,request,redirect,url_for,abort
from . import main
from app.models import User
from werkzeug.security import generate_password_hash


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    View root page function that returns the index page and its data
    '''
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email)
        if user:
            return render_template('signup.html', error=f'User with email {email} already exists')
        new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('signup.html')

