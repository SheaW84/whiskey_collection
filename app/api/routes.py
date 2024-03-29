from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Whiskey, whiskey_schema, whiskeys_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'test':'whiskey'}


#CREATE
@api.route('/whiskeys', methods =['POST'])
@token_required
def create_whiskeys(current_user_token):
    brand = request.json['brand']
    origin = request.json['origin']
    variety = request.json['variety']
    year = request.json['year']
    user_token = current_user_token.token

    print(f'{current_user_token.token}')

    whiskey = Whiskey(brand, origin, variety, year, user_token = user_token)

    db.session.add(whiskey)
    db.session.commit()

    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

#READ ALL
@api.route('/whiskeys', methods =['GET'])
@token_required
def get_whiskeys(current_user_token):
    a_user = current_user_token.token
    whiskeys = Whiskey.query.filter_by(user_token = a_user).all()
    response = whiskeys_schema.dump(whiskeys)
    return jsonify(response)

#READ ONE
@api.route('/whiskeys/<id>', methods=['GET'])
@token_required
def get_one_whiskey(current_user_token, id):
    whiskey = Whiskey.query.get(id)
    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

#UPDATE
@api.route('/whiskeys/<id>', methods =['POST','PUT'])
@token_required
def update_whiskey(current_user_token,id):
    whiskey = Whiskey.query.get(id)
    whiskey.brand = request.json['brand']
    whiskey.origin = request.json['origin']
    whiskey.variety = request.json['variety']
    whiskey.year = request.json['year']
    whiskey.user_token = current_user_token.token

    db.session.commit()
    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

#DELETE
@api.route('/whiskeys/<id>', methods=['DELETE'])
@token_required
def delete_whiskey(current_user_token,id):
    whiskey = Whiskey.query.get(id)
    db.session.delete(whiskey)
    db.session.commit()
    response = whiskey_schema.dump(whiskey)
    return jsonify(response)
