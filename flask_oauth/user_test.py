from .conftest import client, set_up_db, tear_down_db
from .user import User

def test_create_user(client, set_up_db):
    username = "Test User"
    user = User(username=username, email="email@email.com")

    user.create_user()
    
    users = User.query.filter_by(username=username)
    assert len(users.all()) == 1

