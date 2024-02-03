from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Whiskey, whiskey_schema, whiskeys_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'test':'whiskey'}

@api.route('/whiskeys', methods =['POST'])
@token_required
def get_whiskeys(current_user_token):
    brand = request.json['brand']
    
