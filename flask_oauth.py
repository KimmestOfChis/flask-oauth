from flask import Flask, request, jsonify
# from models.users import User
# from models.db import db
from api.user_api import user_api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models.users import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.register_blueprint(user_api)
db.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)

