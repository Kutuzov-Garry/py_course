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


>>> def b(x):
	try:
		a(x)
	except:
		print(321)
		raise

	
>>> b(234)
321
Traceback (most recent call last):
  File "<pyshell#605>", line 1, in <module>
    b(234)
  File "<pyshell#604>", line 3, in b
    a(x)
TypeError: 'int' object is not callable



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

# VS Code debugging.
https://code.visualstudio.com/docs/editor/debugging

# Режим Debug в Shell.
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
