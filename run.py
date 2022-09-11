from app import app, db
from app.blueprints.auth.models import User
from app.blueprints.orders.models import Order
from app.blueprints.cart.models import Cart
from app.blueprints.courier.models import Courier
from app.blueprints.things.models import Product



if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Order': Order,
        'Cart': Cart,
        'Product': Product,
        'Courier': Courier,
    }