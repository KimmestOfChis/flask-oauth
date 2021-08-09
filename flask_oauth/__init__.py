from flask import Flask, jsonify
from .database import db
from .controllers.user_controller import user_controller

def create_app(env=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(user_controller)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/_health', methods=["GET"])
    def health():
        return jsonify({"status": {"app": "OK"}})
    return app
