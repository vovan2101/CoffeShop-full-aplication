import os
import base64
from datetime import datetime, timedelta
from app import db
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)
    phone_number = db.Column(db.String(150), nullable=False)
    home_address = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    data_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    token = db.Column(db.String(32), unique=True, index=True)
    token_expiration = db.Column(db.DateTime)
    orders_id = db.relationship('Order', backref='buyer', lazy = True)
    cart = db.relationship('Cart', backref='user_cart')
    courier_id = db.relationship('Courier', backref='user_id')


    #Hashing users password + adding data in database
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()


    #Checking the real value of hash password
    def check_password(self, password):
        return check_password_hash(self.password, password)


    #Put that data to the dict, so I can see it in JSON format
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'home_address': self.home_address,
            'data_created': self.data_created,
        }


    #Function that gives tokens to users
    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(minutes=1):
            return self.token
        self.token = base64.b64decode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.commit()
        return self.token


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    
    def update(self, data):
        for field in data:
            if field in {'name', 'phone_number', 'email', 'home_address'}:
                setattr(self, field, data[field])
        db.session.commit()  

    
