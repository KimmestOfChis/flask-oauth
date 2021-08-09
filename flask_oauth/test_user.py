import pytest
from .user import User

username = "Test User"
email = "email@email.com"
bad_email = "blah"
password = "a_V@lid_passw0rd"
too_short_password = "1"
password_without_capitals = "a_valid_passw0rd"
password_without_a_number = "a_valid_password"
password_without_special_characters = "validpassword"

def test_create_user():
    User(username=username, email=email, password=password, password_confirm=password).create_user()
    
    user_list = User.query.filter_by(username=username)
    created_user = user_list.first()

    assert len(user_list.all()) == 1
    assert created_user.username == username
    assert created_user.email == email

def test_validates_presence_of_username():
    with pytest.raises(AssertionError) as error:
        user = User(username="", email=email, password=password, password_confirm=password)

        user.create_user()

    assert str(error.value) == "username cannot be blank" 
    assert len(User.query.filter_by(username=username).all()) == 0

def test_validates_uniqueness_of_username():
    User(username=username, email=email, password=password, password_confirm=password).create_user()

    with pytest.raises(AssertionError) as error:
        User(username=username, email=email, password=password, password_confirm=password).create_user()

    assert str(error.value) == "username has been taken" 
    assert len(User.query.filter_by(username=username).all()) == 1

def test_validates_presence_of_email():
    with pytest.raises(AssertionError) as error:
        user = User(username=username, email="")

        user.create_user()

    assert str(error.value) == "email cannot be blank" 
    assert len(User.query.filter_by(username=username).all()) == 0

def test_validates_uniqueness_of_email():
    User(username=username, email=email, password=password, password_confirm=password).create_user()

    with pytest.raises(AssertionError) as error:
        User(username="different username", email=email, password=password, password_confirm=password).create_user()

    assert str(error.value) == "email has been taken" 
    print(User.query.filter_by(email=email).all())
    assert len(User.query.filter_by(email=email).all()) == 1

def test_validates_format_of_email():
    with pytest.raises(AssertionError) as error:
        user = User(username=username, email=bad_email, password=password, password_confirm=password)

        user.create_user()

    assert str(error.value) == "invalid email format" 
    assert len(User.query.filter_by(email=bad_email).all()) == 0

def test_validates_passwords_match():
    with pytest.raises(AssertionError) as error:
        user = User(username=username, email=email, password=password, password_confirm="")

        user.create_user()

    assert str(error.value) == "passwords do not match" 
    assert len(User.query.filter_by(email=bad_email).all()) == 0

    with pytest.raises(AssertionError) as error:
        user = User(username=username, email=email, password="", password_confirm=password)

        user.create_user()

    assert str(error.value) == "passwords do not match" 
    assert len(User.query.filter_by(email=bad_email).all()) == 0

def test_validates_passwords_length():
    with pytest.raises(AssertionError) as error:
        user = User(username=username, email=email, password=too_short_password, password_confirm=too_short_password)

        user.create_user()

    assert str(error.value) == "passwords must be 8 characters long"
    assert len(User.query.filter_by(email=bad_email).all()) == 0

def test_validates_passwords_has_capital_letters():
    with pytest.raises(AssertionError) as error:
        user = User(username=username, email=email, password=password_without_capitals, password_confirm=password_without_capitals)

        user.create_user()

    assert str(error.value) == "passwords must contain both lowercased and capital letters, a special character, and a number"
    assert len(User.query.filter_by(email=bad_email).all()) == 0

def test_validates_passwords_has_a_number():
    with pytest.raises(AssertionError) as error:
        user = User(username=username, email=email, password=password_without_a_number, password_confirm=password_without_a_number)

        user.create_user()

    assert str(error.value) == "passwords must contain both lowercased and capital letters, a special character, and a number"
    assert len(User.query.filter_by(email=bad_email).all()) == 0

def test_validates_passwords_has_a_special_character():
    with pytest.raises(AssertionError) as error:
        user = User(username=username, email=email, password=password_without_special_characters, password_confirm=password_without_special_characters)

        user.create_user()

    assert str(error.value) == "passwords must contain both lowercased and capital letters, a special character, and a number"
    assert len(User.query.filter_by(email=bad_email).all()) == 0

def test_check_password():
    User(username=username, email=email, password=password, password_confirm=password).create_user()
    user = User.query.filter_by(username=username).first()

    assert not user.check_password(too_short_password)
    assert user.check_password(password)

