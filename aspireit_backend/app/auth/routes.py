from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app import mongo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    mongo.db.users.insert_one({'username': data['username'], 'password': hashed_password})
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = mongo.db.users.find_one({'username': data['username']})
    if user and check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity=user['username'])
        return jsonify(access_token=access_token), 200
    return jsonify({'message': 'Invalid credentials'}), 401
