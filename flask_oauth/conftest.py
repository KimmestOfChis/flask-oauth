from . import create_app
from .database import db
import pytest 

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    with app.app_context():
        with app.test_client() as client:
            yield client



@pytest.fixture
def set_up_db():
    db.drop_all()
    db.create_all()

@pytest.fixture
def tear_down_db():
    db.session.remove()
    db.drop_all()
