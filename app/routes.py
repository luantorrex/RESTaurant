# External
import json
from flask import jsonify
from flask.wrappers import Response

# Internal
from app import app, db
from app.models import Order


@app.route('/')
def index():
    return "Welcome to RESTaurant!"


@app.route('/create/<order_name>/<order_description>/', methods=['GET', 'POST'])
@app.route('/create/<order_name>/', defaults={'order_description': 'None'}, 
    methods=['GET', 'POST'])
def create(order_name, order_description):

    try:
        this_order = Order(name=order_name, description=order_description)
        db.session.add(this_order)
        db.session.commit()
        response = {
            'msg': '%s registered on our menu' % order_name.capitalize()
        }

    except:
        response = {
            'msg': 'Error trying to insert % s' % order_name
        }
    
    return jsonify(response)


@app.route('/read/<int:id>/')
def read(id):
    
    try:
        this_order = Order.query.filter_by(id=id).first()
        response = {
            'id': '%s' % this_order.id,
            'name': '%s' % this_order.name,
            'description': '%s' % this_order.description
        }
    except:
        response = {
            'msg': 'Id %s not find' % id
        }

    return jsonify(response)


@app.route('/update/name/<int:id>/<new_var>/')
def update(id, new_var):

    try:
        this_order = Order.query.filter_by(id=id).first()
        this_order.name = new_var
        db.session.add(this_order)
        db.session.commit()
        response = {
            'msg': 'Order successfully changed',
            'id': '%s' % this_order.id,
            'name': '%s' % this_order.name,
            'description': '%s' % this_order.description
        }
    
    except:
        response = {
            'msg': 'We didnt find any order with this id'
        }

    return jsonify(response)


@app.route('/delete/<int:id>/')
def delete(id):

    try:
        this_order = Order.query.filter_by(id=id).first()
        db.session.delete(this_order)
        db.session.commit()

        response = {
            'msg': '%s deleted from our menu' % id
        }

    except:
        response = {
            'msg': 'Id %s not find' % id
        }

    return jsonify(response)