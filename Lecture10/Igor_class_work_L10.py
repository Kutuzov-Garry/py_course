# Igor_class_work_L10

>>> class Car:
	def __init__(self, brand, vol):
		self.brand = brand
		self.volume = vol
	def __str__(self):
		return f"{self.brand}: {self.volume}"

	
>>> my_car = Car("VAZ", 1.8)
>>> print(my_car)
VAZ: 1.8
>>> 

>>> class Car:
	def __init__(kitty, brand, vol):  # можно НО НЕ НУЖНО иные слова вместо соглашения self.
		kitty.brand = brand
		kitty.volume = vol
	def __str__(kitty):
		return f"{kitty.brand}: {kitty.volume}"

	
>>> my_car = Car("VAZ", 1.8)
>>> print(my_car)
VAZ: 1.8
>>> 
>>> class Car:
	def __init__(self, brand, vol):
		self.brand = brand
		self.volume = vol
	def __str__(self):
		return f"{self.brand}: {self.volume}"
	def __repr__(self):
		return f"Inst of Car:\n\tBrand:{self.brand}. \n\tVolume{self.volume}"

	
>>> my_new_car = Car("ZAZ", 0.9)
>>> my_new_car
Inst of Car:
	Brand:ZAZ. 
	Volume0.9
>>> my_new_car.volume = 12.5
>>> my_new_car
Inst of Car:
	Brand:ZAZ. 
	Volume12.5
>>> 
>>> class Car:
	counter = 0
	def __init__(self, brand, vol):
		self.brand = brand
		self.volume = vol
		Car.counter += 1
	def __str__(self):
		return f"{self.brand}: {self.volume}"
	def __repr__(self):
		return f"Inst of Car:\n\tBrand:{self.brand}. \n\tVolume{self.volume}"

	
>>> Car.counter
0
>>> my_new_car = Car("ZAZ", 0.9)
>>> my_new_car = Car("ZAZ", 0.9)
>>> Car.counter
2
>>> Car.__doc__
>>> Car.__bases__
(<class 'object'>,)

>>> e = Empty()
>>> 
>>> my_new_car.__dict__
{'brand': 'ZAZ', 'volume': 0.9}
>>> Car.__dict__
mappingproxy({'__module__': '__main__', 'counter': 2, '__init__': <function Car.__init__ at 0x0000018A6C0CCB70>, '__str__': <function Car.__str__ at 0x0000018A6C0CCBF8>, '__repr__': <function Car.__repr__ at 0x0000018A6C0CCC80>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
>>> Car.__name__
'Car'
>>> 

>>> class Car:
	counter = 0
	def __init__(self, brand, vol):
		self.brand = brand
		self.volume = vol
		Car.counter += 1
	def drive(self, dist):
		print(f"Я проехал {dist} килОметров!")
	def __str__(self):
		return f"{self.brand}: {self.volume}"
	def __repr__(self):
		return f"Inst of Car:\n\tBrand:{self.brand}. \n\tVolume{self.volume}"

	
>>> hasattr
<built-in function hasattr>
>>> setattr
<built-in function setattr>
>>> getattr
<built-in function getattr>
>>> my_new_car
Inst of Car:
	Brand:ZAZ. 
	Volume0.9
>>> my_new_car.brand
'ZAZ'
>>> getattr(my_new_car, "brand")
'ZAZ'
>>> getattr(my_new_car, "bra", False)
False
>>> res = getattr(my_new_car, "bra", False)
>>> res
False
>>> res = getattr(my_new_car, "brand")
>>> res
'ZAZ'
>>> if getattr(my_new_car, "brand") != False:  # Извлечь атрибут в виде строки.
	print(my_new_car.brand)

	
ZAZ
>>> hasattr(my_new_car, "brand")
True
>>> hasattr(my_new_car, "brd")
False
>>> if hasattr(my_new_car, "brand"):
	print(my_new_car.brand)

	
ZAZ
>>> if hasattr(my_new_car, "brand"):
	print(my_new_car.brand)
else:
	print(False)

	
ZAZ
>>> if hasattr(my_new_car, "bra"):
	print(my_new_car.brand)
else:
	print(False)

	
False
>>> 

>>> setattr(my_new_car, "bra", 123)
>>> my_new_car.__dict__
{'brand': 'ZAZ', 'volume': 0.9, 'bra': 123}
>>> setattr(my_new_car, "bravo", 1234)
>>> my_new_car.__dict__
{'brand': 'ZAZ', 'volume': 0.9, 'bra': 123, 'bravo': 1234}
>>> 


>>> class Animal:
	def __init__(self, color, age):
		self.color = color
		self.age = age
	def eat(self):
		print(f"Животное {self.color} цвета кушает...")
	def go(self):
		print("Животное двигается")
	def sleep(self):
		print("Zzzzz...")

		
>>> class DomesticCat(Animal):
	def __init__(self, name, color, age):
		self.name = name
		super().__init__(color, age)

		
>>> cat = DomesticCat("Dima", "black", 0)
>>> cat.color
'black'
>>> cat.name
'Dima'
>>> cat.age
0
>>> cat.eat()
Животное black цвета кушает...
>>> cat.sleep()
Zzzzz...
>>> cat.go()
Животное двигается
>>> 

>>> 
>>> >>> class DomesticCat(Animal):
	def __init__(self, name, color, age):
		self.name = name
		super().__init__(color, age)
	def __repr__(self):
		return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

	
>>> cat = DomesticCat("Dima", "black", 0)
>>> cat
Cat Name:Dima
	Age:0
	Color:black
>>> 
>>> 
>>> 
>>> class DomesticCat(Animal):
	counter = 123
	def __init__(self, name, color, age):
		self.name = name
		self.id = DomesticCat.counter
		DomesticCat.counter += 1
		super().__init__(color, age)
	def __repr__(self):
		return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

	
>>> cat = DomesticCat("Dima", "black", 0)
>>> cat.id
123
>>> cat.id = 222
>>> cat.id
222
>>> class DomesticCat(Animal):
	counter = 123
	def __init__(self, name, color, age):
		self.name = name
		self._id = DomesticCat.counter
		DomesticCat.counter += 1
		super().__init__(color, age)
	def __repr__(self):
		return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

	
>>> cat = DomesticCat("Dima", "black", 0)
>>> cat.__dict__
{'name': 'Dima', '_id': 123, 'color': 'black', 'age': 0}
>>> cat._id = 333
>>> cat._id
333
>>> class DomesticCat(Animal):
	counter = 123
	def __init__(self, name, color, age):
		self.name = name
		self.id_ = DomesticCat.counter
		DomesticCat.counter += 1
		super().__init__(color, age)
	def __repr__(self):
		return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

	
>>> cat = DomesticCat("Dima", "black", 0)
>>> cat.__dict__
{'name': 'Dima', 'id_': 123, 'color': 'black', 'age': 0}
>>> cat._id = 444
>>> cat._id
444
>>> 
>>> class DomesticCat(Animal):
	counter = 123
	def __init__(self, name, color, age):
		self.name = name
		self.__id = DomesticCat.counter
		DomesticCat.counter += 1
		super().__init__(color, age)
	def __repr__(self):
		return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

	
>>> cat = DomesticCat("Dima", "black", 0)
>>> cat._id
Traceback (most recent call last):
  File "<pyshell#642>", line 1, in <module>
    cat._id
AttributeError: 'DomesticCat' object has no attribute '_id'
>>> 
>>> 
>>> class DomesticCat(Animal):
	counter = 123
	def __init__(self, name, color, age):
		self.name = name
		self.__id = DomesticCat.counter
		DomesticCat.counter += 1
		super().__init__(color, age)
	def get_id(self):
		print(f"cat id is: {self.__id}")
	def __repr__(self):
		return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

	
>>> cat = DomesticCat("Dima", "black", 0)
>>> cat.__id
Traceback (most recent call last):
  File "<pyshell#648>", line 1, in <module>
    cat.__id
AttributeError: 'DomesticCat' object has no attribute '__id'
>>> 

# https://github.com/pallets/flask это основной фреймворк.
# https://github.com/fastapi/fastapi это другой фреймворк.


# Stack - Стек - в отдельном файле stack.py.


# Special methods.
>>> a = 10
>>> b = 11
>>> a + b
21
>>> a.__add__(b)
21
>>> a - b
-1
>>> a.__sub__(b)
-1
>>> a / b
0.9090909090909091
>>> a.__truediv__(b)
0.9090909090909091
>>> s = "abc"
>>> 
>>> 

>>> class Cat:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __add__(self, nextcat):
		return self.age + nextcat.age
	def __contains__(self, key):
		return key in self.name
	def __len__(self):
		return self.age
	def __lt__(self, nextcat):
		return self.age < nextcat.age

	
>>> c = Cat("Cat", 5)
>>> c2 = Cat("Sanya", 6)
>>> c + c2
11
>>> len(c)
5
>>> len(c2)
6
>>> c < c2
True
>>> c2 < c
False
>>> "a" in c
True
>>> "d" in c
False
>>> 
>>> 
>>> c
<__main__.Cat object at 0x0000018A6C0E9518>
>>> 
>>> 
>>> class Wallet:
	def __init__(self, amount):
		self.amount = amount
	def __add__(self, int_value):
		return self.amount + int_value
	def __sub__(self, int_value):
		return self.amount - int_value
	def __len__(self):
		return self.amount

	
>>> my_wallet = Wallet(1000)
>>> class Wallet:
	def __init__(self, amount):
		self.amount = amount
	def __add__(self, int_value):
		self.amount += int_value
		return self.amount
	def __sub__(self, int_value):
		self.amount -= int_value
		return self.amount
	def __len__(self):
		return self.amount

	
>>> my_wallet = Wallet(1000)
>>> my_wallet + 100
1100
>>> len(my_wallet)
1100
>>> my_wallet - 50
1050
>>> len(my_wallet)
1050

# https://docs.python.org/3/reference/datamodel.html#special-method-names .
