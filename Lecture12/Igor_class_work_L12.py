# Igor_class_work_L12.

# Передача нескольких аргументов в Функцию.
print()

print(1,2,3)
1 2 3
print(2)
2
def Pront(values):
    for val in vals:
        print(val, end=" ")
    print()

    
def Pront(values):
    for val in values:
        print(val, end=" ")
    print()

    
Pront([1,2,3,4])
1 2 3 4 
Pront("fsfsdf")
f s f s d f 
Pront(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#324>", line 1, in <module>
    Pront(1,2,3,4,5)
TypeError: Pront() takes 1 positional argument but 5 were given
Pront(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    Pront(1,2,3,4)
TypeError: Pront() takes 1 positional argument but 4 were given
print(1,2,3,4)
1 2 3 4
def Pront(values):
    for val in values:
        print(val, end=" ")
    print()

    
def Pront(*values):
    for val in values:
        print(val, end=" ")
    print()

    
Pront(1,2,3,4,5)
1 2 3 4 5 

def Pront(*values):
    print(type(values))
    
    for val in values:
        print(val, end=" ")
    print()

    
Pront(1,2,3,4,5)
<class 'tuple'>
1 2 3 4 5 
Pront(1,2,3,4,5, [1,2,3,4], "sdfsf")
<class 'tuple'>
1 2 3 4 5 [1, 2, 3, 4] sdfsf 
print(1,2,3,4,5, [1,2,3,4], "sdfsf")
1 2 3 4 5 [1, 2, 3, 4] sdfsf

def Pront(*args):
    print(type(args))
    
    for val in args:
        print(val, end=" ")
    print()

    
Pront(1,2,3,4,5, [1,2,3,4], "sdfsf")
<class 'tuple'>
1 2 3 4 5 [1, 2, 3, 4] sdfsf 
Pront([1,2,3,4,5])
<class 'tuple'>
[1, 2, 3, 4, 5] 
# Pront(1,2,3,4,5, [1,2,3,4], "sdfsf").

def Pront(*args):
    print(type(args))
    print(args)
    
    for val in args:
        print(val, end=" ")
    print()

    
Pront(1,2,3,4,5, [1,2,3,4,5], "sdfsf")
<class 'tuple'>
(1, 2, 3, 4, 5, [1, 2, 3, 4, 5], 'sdfsf')
1 2 3 4 5 [1, 2, 3, 4, 5] sdfsf 


a,b, *c = [1,2,3,4,5,6]
c
[3, 4, 5, 6]

def Pront(*args, sep1=" ", end1="\n"):

    for val in args:
        print(val, end = sep1)
    print(end=end1)

    
Pront(1,2,3,4,5, [1,2,3,4,5], "sdfsf")
1 2 3 4 5 [1, 2, 3, 4, 5] sdfsf


def balances(**balance):
    print(balance)
    print(type(balance))
    for k, w in balance.items():
        print("\t", k, ":", w)
    print()

    
balances(1,2,3,4,4)
Traceback (most recent call last):
  File "<pyshell#372>", line 1, in <module>
    balances(1,2,3,4,4)
TypeError: balances() takes 0 positional arguments but 5 were given

balances(name="Vasia", cash=120000)
{'name': 'Vasia', 'cash': 120000}
<class 'dict'>
	 name : Vasia
	 cash : 120000

def numbers(name="Joe", *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

    

numbers()
Joe
()
{}
# Это дефолтовые значения для * и **.

def numbers(args, kwargs, name="Joe"):
    print(name)
    print(args)
    print(kwargs)

    
numbers()
Traceback (most recent call last):
  File "<pyshell#387>", line 1, in <module>
    numbers()
TypeError: numbers() missing 2 required positional arguments: 'args' and 'kwargs'

def numbers(name="Joe", *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

    
numbers()
Joe
()
{}
numbers("Vasya", 1,2,3,34,5,6,7,8,"sdfsdf", age=100, apples=99)
Vasya
(1, 2, 3, 34, 5, 6, 7, 8, 'sdfsdf')
{'age': 100, 'apples': 99}


def numbers(name="Joe", **kwargs, *args):
    print(name)
    print(args)
    print(kwargs)
    
SyntaxError: invalid syntax

def numbers(name="Joe", *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

    
def num_sum(*args):
    s = 0
    for i in args:
        s += i
    print(s)

    
def numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    num_sum(args)

    
numbers(1,2,3,4,5,6)
(1, 2, 3, 4, 5, 6)
{}
Traceback (most recent call last):
  File "<pyshell#406>", line 1, in <module>
    numbers(1,2,3,4,5,6)
  File "<pyshell#405>", line 4, in numbers
    num_sum(args)
  File "<pyshell#402>", line 4, in num_sum
    s += i
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'

def numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    num_sum(*args)  # Добавили * перед args (иначе Кортеж в Кортеж).

    
numbers(1,2,3,4,5,6)
(1, 2, 3, 4, 5, 6)
{}
21

li1, li2 = [1,2,3], [4,5,6]
li1
[1, 2, 3]
li2
[4, 5, 6]
li3 = li1 + li2
li3
[1, 2, 3, 4, 5, 6]
li3 = [li1, li2]
li3
[[1, 2, 3], [4, 5, 6]]
li3 = [*li1, *li2]
li3
[1, 2, 3, 4, 5, 6]

st = "sdfsdfsdf"
li = [st]
li
['sdfsdfsdf']
li = [*st]
li
['s', 'd', 'f', 's', 'd', 'f', 's', 'd', 'f']
di = {"1":2, "2":3}
di = {"11":22, "22":33}
di1 = {"1":2, "2":3}
di3 = {**di, **di1}
di3
{'11': 22, '22': 33, '1': 2, '2': 3}
*ttt, = "sdfsdfsdf"
ttt
['s', 'd', 'f', 's', 'd', 'f', 's', 'd', 'f']
ttt
['s', 'd', 'f', 's', 'd', 'f', 's', 'd', 'f']
*ttt = "sdfsdfsdf"
SyntaxError: starred assignment target must be in a list or tuple
простба экран вниз
SyntaxError: invalid syntax. Perhaps you forgot a comma?

a, *ttt = "fsdfsdfs"
a
'f'
ttt
['s', 'd', 'f', 's', 'd', 'f', 's']
*ttt, = "fsdfsdfs"
ttt
['f', 's', 'd', 'f', 's', 'd', 'f', 's']


# 1й перерыв.

# lambda.
# b^2 - 4*a*c дискриминант.
def D(b, a, c):
    return b**2 - 4*a*c

D
<function D at 0x00000198E4DC6A70>

lambda: 2
<function <lambda> at 0x00000198E4DC6B90>
def retTwo():
    return 2

retTwo()
2
lambda a,b,c: a*b-c
<function <lambda> at 0x00000198E4DC6B90>

(lambda a,b,c: a*b-c) ()
Traceback (most recent call last):
  File "<pyshell#461>", line 1, in <module>
    (lambda a,b,c: a*b-c) ()
TypeError: <lambda>() missing 3 required positional arguments: 'a', 'b', and 'c'

(lambda a,b,c: a*b-c) (2,3,4)  # Дали три аргумента.
2

def cond(z,x,y, b,a,c):
    return z+x+y + (lambda b, a, c: b**2 - 4*a*c)(b,a,c)

cond(1,2,3, 4,3,5)
-38


# Iterators.
li = [2,3,4,5,7]
for i in li:
    print(i)

    
2
3
4
5
7
li_iter = iter(li)
li_iter
<list_iterator object at 0x00000198E4DAA350>
next(li_iter)
2
next(li_iter)
3
next(li_iter)
4
next(li_iter)
5
next(li_iter)
7
next(li_iter)
Traceback (most recent call last):
  File "<pyshell#482>", line 1, in <module>
    next(li_iter)
StopIteration

st = "sdfsdf"
st_iter = iter(st)
st_iter
<str_iterator object at 0x00000198E4DA8F40>
next(st_iter)
's'
next(st_iter)
'd'
next(st_iter)
'f'
next(st_iter)
's'
next(st_iter)
'd'
next(st_iter)
'f'
next(st_iter)
Traceback (most recent call last):
  File "<pyshell#493>", line 1, in <module>
    next(st_iter)
StopIteration


class powFive:
    def __init__(self, maxn):
        self.maxn = maxn

        
class PowFive:
    def __init__(self, maxn):
        self.maxn = maxn
    def __iter__(self):
        self.counter = 1
        return self
    def __next__(self):
        if self.counter <= self.maxn:
            res = 5 ** self.counter
            self.counter += 1
            return res
        raise StopIteration


p = PowFive(4)
p
<__main__.PowFive object at 0x00000198E4DA9ED0>
p_iter = iter(p)
next(p_iter)
5
next(p_iter)
25
next(p_iter)
125
next(p_iter)
625
next(p_iter)
Traceback (most recent call last):
  File "<pyshell#535>", line 1, in <module>
    next(p_iter)
  File "<pyshell#510>", line 12, in __next__
    raise StopIteration
StopIteration


# Generator.
li = [i**2 for i in ranfe(10)]
Traceback (most recent call last):
  File "<pyshell#538>", line 1, in <module>
    li = [i**2 for i in ranfe(10)]
NameError: name 'ranfe' is not defined. Did you mean: 'range'?
li = [i**2 for i in range(10)]
li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
gen = [i**2 for i in range(10)]
gen
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# yield.
def retNumbers(n):
    for i in range(n):
        return i

    
retNumbers(5)
0
retNumbers(5)
0
retNumbers(5)
0
def retNumbers(n):
    for i in range(n):
        yield i**2

        
r = retNumbers(5)
r
<generator object retNumbers at 0x00000198E4D82A40>
next(r)
0
next(r)
1
next(r)
4
next(r)
9
next(r)
16
next(r)
Traceback (most recent call last):
  File "<pyshell#577>", line 1, in <module>
    next(r)
StopIteration


# map.
def mulFive(n):
    return n * 5

li = [1,2,3,4]
res_li = list(map(mulFive, li))
res_li
[5, 10, 15, 20]


# Замыкание!.
def a():
    x = 10
    def inner(number):
        return number**x
    return inner

res = a()
res
<function a.<locals>.inner at 0x00000198E4DC7370>
res(6)
60466176


# nonlocal.
def numPowTwo():
    num = 2
    def inner():
        nonlocal num
        num **= 2
        return num
    return inner

res = numPowTwo()
res()
4
res()
16
res()
256
res()
65536


# Metaclass.
class Dog:
    pass

d = Dog()
type(d)
<class '__main__.Dog'>
type(Dog)
<class 'type'>
isinstance(d, Dog)
True
isinstance(Dog, type)
True
isinstance(int, type)
True
isinstance(list, type)
True

list.__bases__
(<class 'object'>,)


class Number:
    def get_number(self):
        return 55

    
n = Number()
n.Num
Traceback (most recent call last):
  File "<pyshell#643>", line 1, in <module>
    n.Num
AttributeError: 'Number' object has no attribute 'Num'
class Number:
    Num = 99
    def get_number(self):
        return 55

    
n = Number()
n.Num
99
n.get_number
<bound method Number.get_number of <__main__.Number object at 0x00000198E4DAA110>>
n.get_number()
55

def get_number(self):
    return 55


NumberFromType = type("NumberFromType", (object,), {"get_number":get_number, "Num":99, "name":"JOJO"})
NumberFromType
<class '__main__.NumberFromType'>
nn = NumberFromType()
type(nn)
<class '__main__.NumberFromType'>
nn.name
'JOJO'
nn.Num
99
nn.get_number()
55

name = input()
Car
name
'Car'
di = {"VIN":123456, "Body Type":"Sedan", "Counter":0}
new_user_type = type(name, (object,), di)
new_user_type
<class '__main__.Car'>
my_car = new_user_type()
my_car.VIN
123456
my_car.Counter
0
