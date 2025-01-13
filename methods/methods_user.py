import requests
from data import Constants

class UserMethods:
    def create_user(login, password, name):
        data = {
            "email": login,
            "password": password,
            "name": name
        }
        response = requests.post(f'{Constants.BASE_URL}{Constants.CREATE_USER_URL}', data=data)
        return response.status_code, response.json()

    def delete_user(login, password, token):
        data = {
            "email": login,
            "password": password
        }
        headers = {
            'Authorization': token
        }
        requests.delete(f'{Constants.BASE_URL}{Constants.CHANGE_USER_DATA}', data = data, headers = headers)

    def login_user(login, password):
        data ={
            "email": login,
            "password": password
        }
        response = requests.post(f'{Constants.BASE_URL}{Constants.LOGIN_USER_URL}', data = data)
        return response.status_code, response.json()

    def get_user_token(login, password):
        data = {
            "email": login,
            "password": password
        }
        response = requests.post(f'{Constants.BASE_URL}{Constants.LOGIN_USER_URL}', data=data)
        return response.json()["accessToken"]


    def change_users_data(login, password, name, token):
        data ={
            "email": login,
            "password" : password,
            "name": name
        }
        headers = {
            'Authorization': token
        }
        response = requests.patch(f'{Constants.BASE_URL}{Constants.CHANGE_USER_DATA}', data, headers = headers)
        return response.status_code, response.json()


