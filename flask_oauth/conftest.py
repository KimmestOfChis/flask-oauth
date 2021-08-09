from . import create_app
from .database import db
import pytest

@pytest.fixture(autouse=True)
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    
    return app

@pytest.fixture(autouse=True)
def client(app):
    with app.app_context():
        with app.test_client() as client:
            yield client

@pytest.fixture(autouse=True)
def setup(app):
    db.init_app(app)
    db.create_all()

    yield

    db.session.remove()
    db.drop_all()
