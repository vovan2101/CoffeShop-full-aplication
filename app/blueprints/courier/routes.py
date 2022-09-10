from . import bp as courier
from flask import jsonify, request
from .models import Courier

@courier.route('/courier', methods=['GET'])
def get_couriers():
    couriers = Courier.query.all()
    return jsonify(c.to_dict() for c in couriers)


@courier.route('/courier/<int:courier_id>')
def get_courier(courier_id):
    courier = courier.query.get_or_404(courier_id)
    return jsonify(courier.to_dict())
