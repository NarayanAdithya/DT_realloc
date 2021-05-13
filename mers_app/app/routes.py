from app import app
from flask import request,redirect,url_for,render_template


@app.route('/')
@app.route('/home')
def home():
    return "This is home page"