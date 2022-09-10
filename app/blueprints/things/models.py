import os
from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String(25))
    price = db.Column(db.Numeric, nullable=False)
   

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'item': self.items,
            'price': self.price,     
        }
