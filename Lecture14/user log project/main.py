# Igor Lab-14 Rick and Morty logging.

from module import User


def main():
    '''логирование активности юзеров'''
    for i in range(10):
        usr = User(f'Rick-{i}', 'Morty')
        usr.login()
        usr.change_password()


if __name__ == "__main__":
    main()


# login
# change_password
# login
# change_password
# login
# change_password
# login
# change_password
# login
# change_password
# login
# change_password
# login
# change_password
# login
# change_password
# login
# change_password
# login
# change_password
