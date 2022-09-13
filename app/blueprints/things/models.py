import os
from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String(25))
    price = db.Column(db.Numeric, nullable=False)
    cart_prodcuts = db.relationship('Cart', secondary="cart")
    

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        from app.blueprints.cart import Cart
        return {
            'id': self.id,
            'item': self.items,
            'price': self.price,
            'cart': Cart.query.get(self.id)
        }
