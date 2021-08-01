from flask import Flask, jsonify

def create_app(env=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    @app.route('/_health', methods=["GET"])
    def health():
        return jsonify({"status": {"app": "OK"}})
    return app
