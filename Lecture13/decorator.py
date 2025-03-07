# decorator.

def add(a, b):
    return a+b

def decorator(func):
    def inner(ia, ib):
        print("asd")
        ib **=2
        func(ia, ib)
    return inner

add(2,3)
5
@decorator
def add(a, b):
    print(a+b)

    
add(2,3)
asd
11



def decorator(func):
    print("привет из декоратора")
    func()

    
def say():
    print("Как дела?")

    
say()
Как дела?

@decorator
def say():
    print("Как дела?")

    
say()
Как дела?

@decorator
def say():
    print("Как дела?")

    
привет из декоратора
Как дела?

say()
Traceback (most recent call last):
  File "<pyshell#884>", line 1, in <module>
    say()
TypeError: 'NoneType' object is not callable
# Требуется Замыкание!.

def decorator(func):
    def inner():
        print("привет из декоратора")
        func()
    return inner



@decorator
def say():
    print("Как дела?")

    
привет из декоратора
Как дела?

say()
Traceback (most recent call last):
  File "<pyshell#884>", line 1, in <module>
    say()
TypeError: 'NoneType' object is not callable
# Требуется Замыкание!.

def decorator(func):
    def inner():  # Замыкание.
        print("привет из декоратора")
        func()
    return inner  # Замыкание.

@decorator
def say():
    print("Как дела?")

    
say()
привет из декоратора
Как дела?

say()
привет из декоратора
Как дела?


@decorator
def bye():
    print("Пока!")

    
bye()
привет из декоратора
Пока!
say()
привет из декоратора
Как дела?



def decorator(func):
    def inner(dname):
        print("привет из декоратора")
        func(dname)
    return inner

@decorator
def say(name):
    print(f"{name}, Как дела?")

    
say("Петя")
привет из декоратора
Петя, Как дела?
