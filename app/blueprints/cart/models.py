import os
from unicodedata import numeric
from app import db

cart_products = db.Table('cart_products',
    db.Column('cart', db.Integer, db.ForeignKey('cart.id')),
    db.Column('product_price', db.Numeric, db.ForeignKey('product.price')),
    db.Column('product_items', db.String(100), db.ForeignKey('product.items'))
 )

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items_and_price = db.relationship("Product", secondary="cart_products", backref='cart_items_price', lazy = 'select')
    



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

     
    def to_dict(self):
        from app.blueprints.auth import User
        return {   
            'id': self.id,       
            'user_cart': User.query.get(self.user_id),
            'items_and_price': cart_products.query.get(self.items_and_price),
        }

    
    def clear(self):
        db.session.delete(self)
        db.session.commit()


    def update(self, data):
        for field in data:
            if field in {'items_and_price'}:
                setattr(self, field, data[field])
        db.session.commit()  

    def cart(item):
        shopping_cart = {}
        total = 0
        for i in shopping_cart.values():
            total += i
        return shopping_cart


