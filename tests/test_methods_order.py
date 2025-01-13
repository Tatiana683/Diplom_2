from data import Constants
from methods.methods_user import UserMethods
from methods.methods_order import OrderMethods

class TestCreateOrder:
    def test_create_order_with_authorization(self):
        UserMethods.get_user_token(Constants.LOGIN_USER_1, Constants.PASSWORD_USER_1) # авторизация в профиль юзера
        order_data = OrderMethods.create_order(Constants.CRATER_BUN)
        assert order_data[0] == 200
        assert order_data[1]['success'] == True

    def test_create_order_without_authorization(self):
        order_data = OrderMethods.create_order(Constants.CRATER_BUN)
        assert order_data[0] == 200
        assert order_data[1]['success'] == True

    def test_create_order_with_ingredients(self):
        order_data = OrderMethods.create_order(Constants.FLUORESCENT_BUN)
        assert order_data[0] == 200
        assert order_data[1]['success'] == True

    def test_create_order_without_ingredients(self):
        order_data = OrderMethods.create_order('')
        assert order_data[0] == 400
        assert order_data[1]['success'] == False

    def test_create_order_with_incorrect_ingredient(self):
        order_data = OrderMethods.create_order(Constants.INCORRECT_BUN)
        assert order_data == 500

class TestShowOrders:
    def test_show_order_user_with_authorization(self):
        UserMethods.get_user_token(Constants.LOGIN_USER_1, Constants.PASSWORD_USER_1) # авторизация в профиль юзера
        order_data = OrderMethods.show_creating_orders()
        assert order_data[0] == 200
        assert order_data[1]['success'] == True

    def test_show_order_user_without_authorization(self):
        order_data = OrderMethods.show_creating_orders()
        assert order_data[0] == 200
        assert order_data[1]['success'] == True
