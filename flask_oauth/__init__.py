from flask import Flask, jsonify
from .database import db

def create_app(env=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/_health', methods=["GET"])
    def health():
        return jsonify({"status": {"app": "OK"}})
    return app
