from app import db
from app import login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin,db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(120),index=True,unique=True)
    password_hash=db.Column(db.String(128))
    aadhar=db.Column(db.String(12),index=True,unique=True)
    mobile_number=db.Column(db.String(10),index=True,unique=True)
    pincode=db.Column(db.String(10))
    age=db.Column(db.Integer)
    gender=db.Column(db.String(5))
    passenger_details=db.relationship('passenger',backref='user_travels',lazy='dynamic')
    tickets=db.relationship('ticket',backref='tickets',lazy='dynamic')
    books=db.relationship('books',backref='booked_tickets',lazy='dynamic')
    def __repr__(self):
        return '<User:{} Id:{}>'.format(self.username,self.id)
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class passenger(db.Model):
    __tablename__='passenger'
    passenger_id=db.Column(db.Integer,primary_key=True)
    pnr_no=db.Column(db.String(80),index=True,unique=True)
    seat_number=db.Column(db.Integer)
    reservation_status=db.Column(db.String(10))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    ticket_id=db.Column(db.Integer,db.ForeignKey('ticket.id'))

class train(db.Model):
    __tablename__='train'
    train_no=db.Column(db.Integer,primary_key=True)
    train_name=db.Column(db.String(100))
    arrival_time=db.Column(db.String(100))
    departure_time=db.Column(db.String(100))
    no_Seats_available=db.Column(db.Integer)
    date=db.Column(db.String(100))
    tickets_booked=db.relationship('ticket',backref='tickets_in_train',lazy='dynamic')
    status_seats=db.relationship('train_status',backref='status',lazy='dynamic')
class ticket(db.Model):
    __tablename__='ticket'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    status=db.Column(db.String(10))
    no_of_passenger=db.Column(db.Integer,default=1)
    train_no=db.Column(db.Integer,db.ForeignKey('train.train_no'))
    bookings=db.relationship('books',backref='bookedby',lazy='dynamic')
class train_status(db.Model):
    __tablename__='train_status'
    id=db.Column(db.Integer,primary_key=True)
    train_id=db.Column(db.Integer,db.ForeignKey('train.train_no'))
    a_seats2=db.Column(db.Integer)
    fare1=db.Column(db.Integer)
    fare2=db.Column(db.Integer)
    date=db.Column(db.String(120))
    w_seat1=db.Column(db.Integer)
    w_seats2=db.Column(db.Integer)
    b_seats1=db.Column(db.Integer)
    b_seats2=db.Column(db.Integer)
    a_seats1=db.Column(db.Integer)

class station(db.Model):
    __tablename__='station'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120))

class books(db.Model):
    __tablename__='books'
    id=db.Column(db.Integer,primary_key=True)
    ticket_id=db.Column(db.Integer,db.ForeignKey('ticket.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

class cancellation(db.Model):
    __tablename__='cancellation'
    id=db.Column(db.Integer,primary_key=True)
    passenger_id=db.Column(db.Integer)
    ticket_id=db.Column(db.Integer)

class starts(db.Model):
    __tablename__='startsat'
    id=db.Column(db.Integer,primary_key=True)
    train_no=db.Column(db.Integer,db.ForeignKey('train.train_no'))
    station_no=db.Column(db.Integer,db.ForeignKey('station.id'))

class stopsat(db.Model):
    __tablename__='stopsat'
    id=db.Column(db.Integer,primary_key=True)
    train_no=db.Column(db.Integer,db.ForeignKey('train.train_no'))
    station_no=db.Column(db.Integer,db.ForeignKey('station.id'))
