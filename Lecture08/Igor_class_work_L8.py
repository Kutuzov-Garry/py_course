# Igor_class_work_L8

# Errors.
>>> s = "asd"
>>> s.capitalize()
'Asd'
>>> s.decapitalize()
Traceback (most recent call last):
  File "<pyshell#525>", line 1, in <module>
    s.decapitalize()
AttributeError: 'str' object has no attribute 'decapitalize'

# Обойти краш деления на 0.
>>> 1 /0
Traceback (most recent call last):
  File "<pyshell#526>", line 1, in <module>
    1 /0
ZeroDivisionError: division by zero

>>> try:
	1 / 0
except:
	print(-1)

	
-1
>>> try:  # Всегда первый.
  1/0

except ZeroDivisionError:
  print("ZeroDivisionError x/0")  # Конкретный except - ветка в середине.
except ValueError:
  print("ValueError")  # Конкретный except - ветка в середине.
except:
  print(-1)  # Всегда последний.

# Синтаксические ошибки всегда вручную исправлять.


>>> try:
	13 / 0
except ZeroDivisionError as zde:
	print("ZeroDivisionError x/0", zde.args)
except ValueError as ve:
	print("ValueError", ve.args)
except:
	print(-1)

	
ZeroDivisionError x/0 ('division by zero',)

>>> try:
	raise ZeroDivisionError  # Сгенерировать ошибку.

# Импорт несуществующего модуля.
>>> import boroda
Traceback (most recent call last):
  File "<pyshell#568>", line 1, in <module>
    import boroda
ModuleNotFoundError: No module named 'boroda'
>>> a = 6
>>> if a == 8:
	try:
		import time
	except:
		pass
else:
	print("Делай без time")

	
Делай без time
>>> 
>>> time.sleep(2)
Traceback (most recent call last):
  File "<pyshell#579>", line 1, in <module>
    time.sleep(2)
NameError: name 'time' is not defined
>>> 



>>> try:
	raise ZeroDivisionError  # 1 / 0.
except:
	print("default")

	
default

# Перехват общим частного. А надо конкретные сверху писать.
>>> try:
	raise ZeroDivisionError  # 1 / 0.
except ArithmeticError:
	print("ArithmeticError")
except ZeroDivisionError:
	print("ZeroDivisionError")
except:
	print("default")

	
ArithmeticError
>>> 


# Some useful exceptions.
ZeroDivisionError - /, // и%.

ValueError - int() or float()

TypeError -
short_list = [1]
one_value = short_list[0.5]

AttributeError -
short_list = [1]
short_list.append(2)
short_list.depend(3)

SyntaxError


def a(x):
	try:
		res = int(x)
	except:
		print("123")

		
a(123)
a("")
123
a("#@3")
123

def a(x):
	try:
		res = int(x)
	except:
		print("123")
		raise  # Добавили raise.

	    
a(123)
a("#@3")
123
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a("#@3")
  File "<pyshell#11>", line 3, in a
    res = int(x)
ValueError: invalid literal for int() with base 10: '#@3'


def b(x):
	try:
		a(x)
	except:
		print(321)
		raise

	    
b(234)
b("$%^")
123
321
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b("$%^")
  File "<pyshell#16>", line 3, in b
    a(x)
  File "<pyshell#11>", line 3, in a
    res = int(x)
ValueError: invalid literal for int() with base 10: '$%^'


# ASSERT - оценщик, валидация.

>>> assert 1
>>> assert 0
Traceback (most recent call last):
  File "<pyshell#610>", line 1, in <module>
    assert 0
AssertionError
>>> assert []
Traceback (most recent call last):
  File "<pyshell#611>", line 1, in <module>
    assert []
AssertionError
>>> assert ""
Traceback (most recent call last):
  File "<pyshell#612>", line 1, in <module>
    assert ""
AssertionError
>>> assert "as"
>>> assert [1,2,3]
>>> assert None
Traceback (most recent call last):
  File "<pyshell#615>", line 1, in <module>
    assert None
AssertionError
>>> assert True
>>> assert False
Traceback (most recent call last):
  File "<pyshell#617>", line 1, in <module>
    assert False
AssertionError

# VS Code debugging, pdf p51.
https://code.visualstudio.com/docs/editor/debugging

# Режим Debug в IDLE Shell.
[DEBUG ON]
>>> 
[DEBUG OFF]

# Тесты делать обязательно!!!
# Иначе рост затрат и возможна потеря заказчиков!!!

# Ручное (мануальное) тестирование.
# Автотесты на ПО.
# Юнит-тесты.

# test_.py
# leetcode.com - коды с решениями задач.
# pytest.org
