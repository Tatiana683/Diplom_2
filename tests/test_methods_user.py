from data import Constants
from methods.methods_user import UserMethods
import pytest
from helpers import RandomCred


class TestCreateUser:

    def test_create_original_user(self):
        login = RandomCred.generate_email()
        password = RandomCred.generate_password()
        name = RandomCred.generate_name()
        user_data = UserMethods.create_user(login, password, name)
        assert 200 == user_data[0]
        assert True == user_data[1]['success']
        token = UserMethods.get_user_token(login, password)
        UserMethods.delete_user(login, password, token)

    def test_create_verified_user(self):
        login = Constants.LOGIN_USER_1
        password = "password"
        name = "Username"
        user_data = UserMethods.create_user(login, password, name)
        assert 403 == user_data[0]
        assert "User already exists" == user_data[1]['message']

    @pytest.mark.parametrize(
        'login, password, name',
        [
            ('', RandomCred.generate_password(), RandomCred.generate_name()),
            (RandomCred.generate_email(), '', RandomCred.generate_name()),
            (RandomCred.generate_email(), RandomCred.generate_password(), '')
        ]
    )
    def test_creating_user_without_required_field(self, login, password, name):
        user_data = UserMethods.create_user(login, password, name)
        assert "Email, password and name are required fields" == user_data[1]['message']

class TestAuthorizationUser:

    def test_login_user(self):
        login = Constants.LOGIN_USER_1
        password = Constants.PASSWORD_USER_1
        user_data = UserMethods.login_user(login, password)
        assert 200 == user_data[0]
        assert True == user_data[1]['success']

    @pytest.mark.parametrize(
        'login, password',
        [
            (Constants.LOGIN_USER_1, RandomCred.generate_password()),
            (RandomCred.generate_email(), Constants.PASSWORD_USER_1)
        ]
    )
    def test_login_user_with_incorrect_data(self, login, password):
        user_data = UserMethods.login_user(login, password)
        assert user_data == (401, {"success": False, "message": "email or password are incorrect"})

class TestChangeDataUser:
    @pytest.mark.parametrize(
        'new_email, new_password, new_name',
        [
            (RandomCred.generate_email(), Constants.PASSWORD_USER_2, Constants.NAME_USER_2),
            (Constants.LOGIN_USER_2, RandomCred.generate_password(), Constants.NAME_USER_2),
            (Constants.LOGIN_USER_2, Constants.PASSWORD_USER_2, RandomCred.generate_name())
        ]
    )
    def test_change_user_data_with_authorization(self, new_email, new_password, new_name):
        login = Constants.LOGIN_USER_2
        password = Constants.PASSWORD_USER_2
        name = Constants.NAME_USER_2
        token = UserMethods.get_user_token(login, password)
        change_data = UserMethods.change_users_data(new_email, new_password, new_name, token)
        assert 200 == change_data[0]
        assert True == change_data[1]['success']

        UserMethods.change_users_data(login, password, name, token)

    @pytest.mark.parametrize(
        'new_email, new_password, new_name',
        [
            (RandomCred.generate_email(), Constants.PASSWORD_USER_1, Constants.NAME_USER_1),
            (Constants.LOGIN_USER_1, RandomCred.generate_password(), Constants.NAME_USER_1),
            (Constants.LOGIN_USER_1, Constants.PASSWORD_USER_1, RandomCred.generate_name())
        ]
    )
    def test_change_user_data_without_authorization(self, new_email, new_password, new_name):
        change_data = UserMethods.change_users_data(new_email, new_password, new_name, token='')
        assert change_data == (401, {"success": False, "message": "You should be authorised"})
