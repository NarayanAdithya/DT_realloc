from app import app,db
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,jsonify
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User
from app.forms import LoginForm,RegisterForm
from werkzeug.urls import url_parse
from wtforms.validators import ValidationError
from datetime import datetime

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/logout')
def logout():
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))

@app.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=RegisterForm()
    if form.validate_on_submit():
        user=User(email=form.email.data,username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Successfully Registered',category="success")
        print(form.password.data)
        return redirect(url_for('home'))
    return render_template('registration.html',form=form,title='Register')


@app.route('/contactus')
@login_required
def contact():
    return render_template('Contact.html')


@app.route('/chatpage')
@login_required
def chatpage():
    return render_template('Chat.html')

@app.route('/seatchange')
@login_required
def seatchange():
    return render_template('seat.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Email or Password',category="danger")
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc!='':
            next_page=url_for('home')
        return redirect(next_page)
    return render_template('login.html',title='SignIn',form=form)

