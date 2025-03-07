# Lab. time_stamp.py

import datetime
datetime.datetime.now()
datetime.datetime(2025, 3, 6, 23, 57, 34, 412945)
say.__name__
'inner'
print(datetime.datetime.now())
2025-03-06 23:58:05.601733

def decorator(func):
    def inner(dname):
        print("привет из декоратора")
        print("Время запуска", datetime.datetime.now())
        print("Имя функции которая запускается:", func.__name__)
        func(dname)
    return inner

@decorator
def say(name):
    print(f"{name}, Как дела?")

    
@decorator
def bye(name):
    print(f"{name}, Пока!")

    
say("Petya")
привет из декоратора
Время запуска 2025-03-06 23:59:11.922113
Имя функции которая запускается: say
Petya, Как дела?

bye("Petya")
привет из декоратора
Время запуска 2025-03-06 23:59:34.087309
Имя функции которая запускается: bye
Petya, Пока!
