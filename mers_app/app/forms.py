from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,RadioField,SelectField,TextAreaField
from wtforms.fields.html5 import EmailField,URLField,DateField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,URL,Length
from app.models import User
from flask_login import current_user,login_user,logout_user,login_required

class LoginForm(FlaskForm):
    email=EmailField('Email',validators=[DataRequired(),Email()],render_kw={'class':'form-control form-group','placeholder':'email'})
    password=PasswordField('Password',validators=[DataRequired()],render_kw={'class':'form-control form-group','placeholder':'password'})
    remember_me=BooleanField('Keep Me Signed In')
    submit=SubmitField('Sign In',render_kw={'class':'btn btn-primary','style':'height : 50px;'})

class RegisterForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()],render_kw={'class':'form-control form-group','placeholder':'Username'})
    email=EmailField('Email',validators=[DataRequired(),Email()],render_kw={'class':'form-control form-group','placeholder':'Email'})
    password=PasswordField('Password',validators=[DataRequired()],render_kw={'class':'form-control form-group','placeholder':'Password'})
    conpassword=PasswordField('Re-Enter Password',validators=[DataRequired(),EqualTo('password')],render_kw={'class':'form-control form-group','placeholder':'Re-Enter Password'})#('values','label')
    submit=SubmitField('Sign In',render_kw={'class':'btn btn-primary','style':'height : 50px;'})
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please Use a Different Username.')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please Use A different Email Address')