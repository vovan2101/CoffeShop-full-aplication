from datetime import datetime
from app import db




class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    items = db.Column(db.String, db.ForeignKey('product.items'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    courier_id = db.relationship('Courier', backref='courier')
    price = db.Column(db.Numeric, db.ForeignKey('product.price'))


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()


    def to_dict(self):
        from app.blueprints.things import Product
        from app.blueprints.courier import Courier
        from app.blueprints.auth import User
        return {
            'id': self.id,
            'data_created': self.data_created,
            'buyer': User.query.get(self.user_id),
            'courier': Courier.query.get(self.courier_id),
            'items': Product.query.get(self.items),
            'order_price': Product.query.get(self.price)
        }