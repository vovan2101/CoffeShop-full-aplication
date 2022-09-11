from app import db


class Courier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        from app.blueprints.orders import Order
        from app.blueprints.auth import User
        return {
            'id': self.id,
            'name': self.name,
            'order_id': Order.query.get(self.order_id),
            'user_courier': User.query.get(self.user_id)
        }
