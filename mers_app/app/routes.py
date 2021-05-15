from app import app
from flask import request,redirect,url_for,render_template


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/registration')
def register():
    return render_template('Registration.html')
    

@app.route('/contactus')
def contact():
    return render_template('Contact.html')


@app.route('/chatpage')
def chatpage():
    return render_template('Chat.html')