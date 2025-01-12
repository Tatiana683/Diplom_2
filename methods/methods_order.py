import requests
from data import Constants

class OrderMethods:
    def create_order(ingredient):
        data = {
            "ingredients": ingredient
        }
        response = requests.post(f'{Constants.BASE_URL}{Constants.CREATE_ORDER}', data = data)
        if response.status_code == 500:
            return response.status_code
        else:
            return response.status_code, response.json()


    def show_creating_orders():
        response = requests.get(f'{Constants.BASE_URL}{Constants.SHOW_LIST_ORDERS}')
        return response.status_code, response.json()
