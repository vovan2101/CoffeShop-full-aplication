from . import bp as product
from flask import jsonify, request
from .models import Product


@product.route('/product')
def get_items():
    items = Product.query.all()
    return jsonify(i.to_dict() for i in items)


@product.route('/product/<int:product_id>')
def get_item(product_id):
    item = Product.query.get_or_404(product_id)
    return jsonify(item.to_dict())