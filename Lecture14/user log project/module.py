# Igor Lab-14 Module for user's logging.


import logging

FORMAT = "%(levelname)s - %(message)s"  # формат вывода логируемых данных.

logger = logging.getLogger("user activity")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("user_activity.log", mode="a")
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)

# декоратор.
def decorate_user_activity(func):
    def int_wrapper(usr):
        message = f"User: {usr.name} {usr.surname}. Completed --> {func.__name__}"
        logger.debug(message)
        func(usr)
    return int_wrapper


class User:  # имя фамилия пользователя.
    def __init__(self, n, s):
        self.name = n
        self.surname = s

    
    @decorate_user_activity
    def login(self):  # декоратор для Логина.
        print("login")

    
    @decorate_user_activity
    def change_password(self):  # декоратор для Смены пароля.
        print("change_password")
