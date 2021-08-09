from flask_oauth.models.user import User
from flask import Blueprint, json, jsonify, request

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/register', methods=["POST"])
def register():
    params = request.json
    try:
        User(username=params['username'], email=params['email'], password=params['password'], password_confirm=params['password_confirm']).create_user()
        return jsonify({"message": f"User {params['username']} created"})
    except AssertionError as e:
        return jsonify({"error": f"{e}"})

