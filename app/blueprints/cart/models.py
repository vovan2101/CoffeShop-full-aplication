import os
from app import db



class Cart(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    items = db.Column(db.String, db.ForeignKey('product.items'))
    price = db.Column(db.Numeric, db.ForeignKey('product.price'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

     
    def to_dict(self):
        from app.blueprints.things import Product
        from app.blueprints.auth import User
        return {   
            'id': self.id,       
            'items': Product.query.get(self.items),
            'user_cart': User.query.get(self.user_id),
            'price': Product.query.get(self.price)
        }

    
    def clear(self):
        db.session.delete(self)
        db.session.commit()


    def update(self, data):
        for field in data:
            if field in {'items'}:
                setattr(self, field, data[field])
        db.session.commit()  

    
