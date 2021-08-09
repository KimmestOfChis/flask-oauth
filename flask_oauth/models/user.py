from flask_oauth.database import db
import re 
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = ""
    password_confirm = ""
    password_hash = db.Column(db.String(128), unique=False, nullable=False)

    def __repr__(self):
        return "<User(id='%s', username='%s', email='%s')>" % (self.id, self.username, self.email)
    
    def create_user(self):
        self.validate_username()
        self.validate_email()
        self.validate_password()
        self.set_password()
        db.session.add(self)
        db.session.commit()

    def validate_username(self):
        if not self.username:
            raise AssertionError("username cannot be blank")

        if User.query.filter_by(username=self.username).first() is not None:
            raise AssertionError("username has been taken")
    
    def validate_email(self):
        if not self.email:
            raise AssertionError("email cannot be blank")

        if User.query.filter_by(email=self.email).first() is not None:
            raise AssertionError("email has been taken")

        if not re.match("[^@]+@[^@]+.[^@]+", self.email):
            raise AssertionError("invalid email format")
    
    def validate_password(self):
        if self.password != self.password_confirm:
            raise AssertionError("passwords do not match")

        if len(self.password) < 8:
            raise AssertionError("passwords must be 8 characters long")
        
        if not bool(re.search(r'\d', self.password)) or not bool(re.search(r'[A-Z]', self.password)) or not bool(re.search(r'[_#?!@$%^&*-]', self.password)):
            raise AssertionError("passwords must contain both lowercased and capital letters, a special character, and a number")
        
    def set_password(self):
        self.password_hash = generate_password_hash(self.password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)