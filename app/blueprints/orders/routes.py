from . import bp as order
from flask import jsonify, request
from .models import Order
from app.blueprints.auth.http_auth import token_auth


#Create order
@order.route('/order', methods=['POST'])
@token_auth.login_required
def create_order():
    data = request.json
    #Check if order not empty
    for field in ['items']:
        if field not in data:
            return jsonify({'error': f'You have to add atleast one item to your cart'}), 400
    # If order not empty
    current_user = token_auth.current_user()
    # Here we we store user_id which have made order
    data['user_id'] = current_user.id
    # Here is a data about order
    new_order = Order(**data)
    # place information in dict as JSON and return it
    return jsonify(new_order.to_dict()), 201


#Get all orders
@order.route('/orders')
def get_orders():
    #Take all data from Order
    orders = Order.query.all()
    #Return that data from to_dict as JSON
    return jsonify(o.to_dict() for o in orders)

#Get one Order by id
@order.route('/order/<int:order_id>')
def get_order(order_id):
    #Getting an order or if order not exist, give an error 404
    order = Order.query.get_or_404(order_id)
    #Return data from to_dict as JSON
    return jsonify(order.to_dict())