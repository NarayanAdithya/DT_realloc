import logging
from flask import Flask
from config import config

#App Initializations
app=Flask(__name__)
app.config.from_object(config)

#Logging Setup
logging.basicConfig(level=logging.DEBUG)

#Login Setup

#DB Setup



from app import routes,models