from crypt import methods
from . import bp as cart
from flask import jsonify, request
from .models import Cart
from app.blueprints.auth.http_auth import token_auth



@cart.route('/cart', methods=['POST'])
@token_auth.login_required
def create_cart():
    data = request.json
    current_user = token_auth.current_user()
    data['user_id'] = current_user.id
    cart = Cart(**data)
    return jsonify(cart.to_dict()), 201


@cart.route('/carts')
def get_carts():
    carts = Cart.query.all()
    return jsonify(c.to_dict() for c in carts)


@cart.route('/cart/<int:cart_id>')
def get_cart(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    return jsonify(cart.to_dict())


@cart.route('/add', methods=['POST'])
def add_product_to_cart(item_name, item_price):
    cart_items = []
    cart_total = 0
    cart_summary = dict((item, cart_items.count(item)) for item in cart_items)
    return 
