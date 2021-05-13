import os
basdir=os.path.abspath(os.path.dirname(__file__))

class config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'fosjo23#$JI$BAE'
    