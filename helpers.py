import random
import string

class RandomCred:
    def generate_email():
        address = "test_klinovskaya_"
        domain = random.choice(["yandex.ru", "gmail.com", "bk.ru"])
        new_login = f'{address}{random.randint(100, 999)}@{domain}'
        return new_login

    def generate_password():
        new_password = f'{random.randint(100000, 999999)}'
        return new_password

    def generate_name():
        length = 9
        all_symbols = string.ascii_uppercase + string.digits
        name = ''.join(random.choice(all_symbols) for _ in range(length))
        return name
