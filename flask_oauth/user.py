from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # password_hash = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def create_user(self):
        self.validate_username()
        db.session.add(self)
        db.session.commit()

    def validate_username(self):
        if not self.username:
            raise AssertionError("username was not provided")