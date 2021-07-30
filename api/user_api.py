from flask import Blueprint, jsonify, request
from models.user import User
from sqlalchemy.exc import SQLAlchemyError

user_api = Blueprint('user_api', __name__)

@user_api.route('/register', methods=["POST"])
def register():
    params = request.json
    
    if params['password'] != params['password_confirm']:
        return jsonify({'error': 'passwords do not match'})
    
    try:
        User.create_user(params['username'], params['email'], params['password'])
        return jsonify({'info': f'user created'})
    except AssertionError as e:
        return jsonify({'error': f'error creating user: {e}'})



