import logging
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
#App Initializations
app=Flask(__name__)
app.config.from_object(config)

#Logging Setup
logging.basicConfig(level=logging.DEBUG)

#Login Setup
login=LoginManager(app)
login.login_view='login'
login.message='Please Login To Access The Page'
login.login_message_category='info'
#DB Setup
db=SQLAlchemy(app)
migrate=Migrate(app,db)


from app import routes,models