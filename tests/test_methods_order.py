from data import Constants
from methods.methods_user import UserMethods
from methods.methods_order import OrderMethods

class TestCreateOrder:
    def test_create_order_with_authorization(self):
        UserMethods.get_user_token(Constants.LOGIN_USER_1, Constants.PASSWORD_USER_1) # авторизация в профиль юзера
        order_data = OrderMethods.create_order(Constants.CRATER_BUN)
        assert 200 == order_data[0]
        assert True == order_data[1]['success']

    def test_create_order_without_authorization(self):
        order_data = OrderMethods.create_order(Constants.CRATER_BUN)
        assert 200 == order_data[0]
        assert True == order_data[1]['success']

    def test_create_order_with_ingredients(self):
        order_data = OrderMethods.create_order(Constants.FLUORESCENT_BUN)
        assert 200 == order_data[0]
        assert True == order_data[1]['success']

    def test_create_order_without_ingredients(self):
        order_data = OrderMethods.create_order('')
        assert 400 == order_data[0]
        assert False == order_data[1]['success']

    def test_create_order_with_incorrect_ingredient(self):
        order_data = OrderMethods.create_order(Constants.INCORRECT_BUN)
        assert 500 == order_data

class TestShowOrders:
    def test_show_order_user_with_authorization(self):
        UserMethods.get_user_token(Constants.LOGIN_USER_1, Constants.PASSWORD_USER_1) # авторизация в профиль юзера
        order_data = OrderMethods.show_creating_orders()
        assert 200 == order_data[0]
        assert True == order_data[1]['success']

    def test_show_order_user_without_authorization(self):
        order_data = OrderMethods.show_creating_orders()
        assert 200 == order_data[0]
        assert True == order_data[1]['success']
