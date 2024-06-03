from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.main.models import BufferObject
from app import mongo
from app.ml.model import analyze_sentiment

main_bp = Blueprint('main', __name__)

@main_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user = get_jwt_identity()
    user = mongo.db.users.find_one({'username': current_user})
    return jsonify({'username': user['username']}), 200

@main_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user = get_jwt_identity()
    data = request.get_json()
    mongo.db.users.update_one({'username': current_user}, {'$set': data})
    return jsonify({'message': 'Profile updated successfully'}), 200

@main_bp.route('/buffer', methods=['POST'])
@jwt_required()
def upload_buffer():
    current_user = get_jwt_identity()
    data = request.get_json()
    buffer_object = BufferObject(
        user_id=current_user,
        buffer_type=data['buffer_type'],
        buffer_data=data['buffer_data']
    )
    mongo.db.buffers.insert_one(buffer_object.to_dict())
    return jsonify({'message': 'Buffer object uploaded successfully'}), 201

@main_bp.route('/buffer/<buffer_id>', methods=['GET'])
@jwt_required()
def get_buffer(buffer_id):
    buffer_object = mongo.db.buffers.find_one({'_id': ObjectId(buffer_id)})
    if buffer_object:
        return jsonify(BufferObject.from_dict(buffer_object).to_dict()), 200
    return jsonify({'message': 'Buffer object not found'}), 404


@main_bp.route('/analyze', methods=['POST'])
@jwt_required()
def analyze_text():
    data = request.get_json()
    text = data['text']
    polarity = analyze_sentiment(text)
    return jsonify({'polarity': polarity}), 200