class Constants:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    CREATE_USER_URL = 'auth/register'
    LOGIN_USER_URL = 'auth/login'
    CHANGE_USER_DATA = 'auth/user'
    SHOW_LIST_ORDERS = 'orders/all'
    CREATE_ORDER = 'orders'

    LOGIN_USER_1 = 'klinovskaya.t@bk.ru'
    PASSWORD_USER_1 = '123456'
    NAME_USER_1 = 'Tatiana15'

    LOGIN_USER_2 = 'test_klinovskaya_1515@gmail.com'
    PASSWORD_USER_2 = '123456'
    NAME_USER_2 = 'test_133'

    CRATER_BUN = '61c0c5a71d1f82001bdaaa6c'
    FLUORESCENT_BUN = '61c0c5a71d1f82001bdaaa6d'
    INCORRECT_BUN = '61c0c5a71d1f82001bdaaa6r'

    ERROR_INCORRECT_DATA_CREATE_USER = "Email, password and name are required fields"
    ERROR_INCORRECT_DATA_LOGIN = {"success": False, "message": "email or password are incorrect"}
    ERROR_AUTHORIZATION = {"success": False, "message": "You should be authorised"}
