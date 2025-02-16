# Kuzmichev_Igor_class_work_L6

>>.> li = []
>>> li
[]
>>> type(li)
<class 'list'>
>>> tp = ()  # Создать кортеж.
>>> tp2 = tuple()  # Создать кортеж.
>>> tp
()
>>> tp2
()
>>> type(tp)
<class 'tuple'>
>>> type(tp2)
<class 'tuple'>
>>> tp3 = 2,  # Создать кортеж.
>>> tp3
(2,)
>>> type(tp3)
<class 'tuple'>

# Какой тип переменной?.
>>> isinstance(tp, tuple)
True
>>> isinstance(tp, list)
False
>>> isinstance(tp, int)
False
>>> 

# Индексация кортежа.

>>> n = (1,2,3,4,5)
>>> n[0]
1
>>> n[-1]
5
>>> liN = list(n)
>>> liN[2] = 333
>>> liN
[1, 2, 333, 4, 5]
>>> n
(1, 2, 3, 4, 5)
>>> n = tuple(liN)  # Подмена значения индекса кортежа через иной список.
>>> n
(1, 2, 333, 4, 5)

# Логику кортежа менять нежелательно, как с помощью вложенного списка!.

# Распаковка для кортежа.
>>> t = (1,23,4)
>>> t
(1, 23, 4)
>>> a,b,c = t
>>> a
1
>>> b
23
>>> c
4
# Распаковка для списка.
>>> li = [1,2,3,4]
>>> a,b,c,d = li
>>> a
1
>>> b
2
>>> c
3
>>> d
4
# Распаковка для строки.
>>> s = "abc"
>>> a,b,c = s
>>> s
'abc'
>>> a
'a'
>>> b
'b'
>>> c
'c'

# Поместить в одну переменную больше значений из кортежа - в виде списка.
>>> t = (1,2,3,4,5,6,7)
>>> a,b,c = t
Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    a,b,c = t
ValueError: too many values to unpack (expected 3)
>>> a,*b,c = t
>>> a
1
>>> b
[2, 3, 4, 5, 6]
>>> c
7

>>> # Кортежи в функции.
>>> def numbers():
	return "error:...",1,2,3,4,5

>>> numbers()
('error:...', 1, 2, 3, 4, 5)
>>> err, *tp_n = numbers()
>>> err
'error:...'
>>> tp_n
[1, 2, 3, 4, 5]
>>> 
>>> if err == "error:...":
	print(123)

	
123

# Срезы slices в кортеже.
>>> t
(1, 2, 3, 4, 5, 6, 7)
>>> t[1:5]
(2, 3, 4, 5)
>>> t[1:-1]
(2, 3, 4, 5, 6)
>>> t[::2]
(1, 3, 5, 7)
>>> 
>>> t += (1,)  # Сложить кортеж.
>>> t
(1, 2, 3, 4, 5, 6, 7, 1)
>>> t + t
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
>>> t * 6
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
>>> 
>>> 5 in t
True
>>> 999 in t
False
>>> 

# Добавить индекс в кортеж.
>>> ordersId = (1,2,3,4,5,6,7)
>>> ordersId += (len(ordersId)+1, )
>>> ordersId
(1, 2, 3, 4, 5, 6, 7, 8)
>>> ordersId += (len(ordersId)+1, )
>>> ordersId += (len(ordersId)+1, )
>>> ordersId
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Изменить кортеж - очень прозрачно, легко и просто!.
 >>> t = (1,2,3,4)
>>> t[1:3]
(2, 3)
>>> (155, )
(155,)
>>> (144, )
(144,)
>>> t = (155, ) + t[1:3] + (144, )
>>> t
(155, 2, 3, 144)

>>> t.count(2)  # Сколько 2 в кортеже?.
1
>>> t.index(2)  # Какой индекс у 2 в кортеже?.
1
>>> >>> t.index(144)  # Какой индекс у 144 в кортеже?.
3
>>> del t  # Удалить кортеж можно просто.

# Итерирование кортежей (циклы).
>>> t = (4,3,2,1)
>>> for value in t:
	print(value)

	
4
3
2
1
>>> for value in t:
	if value *2 == 4:
		continue
	print(value)

	
4
3
1
>>> 

# По индексу.
>>> t
(4, 3, 2, 1)
>>> n = len(t)
>>> n
4

>>> for i in range(n):
	print(i, ", value: t[i]")

	
0 , value: t[i]
1 , value: t[i]
2 , value: t[i]
3 , value: t[i]
>>> 
>>> for i in range(n):
	print(i, ", value:", t[i])

	
0 , value: 4
1 , value: 3
2 , value: 2
3 , value: 1
>>> 

# Словари dict.
# Создать пустой.
>>> di = {}
>>> type(di)
<class 'dict'>
>>> di1 = dict()
>>> di1
{}
>>> type(di1)
<class 'dict'>

# hash. хэшируемый - на 99% - это неизменяемый тип.
>>> hash
<built-in function hash>
>>> a = 3
>>> b = 4.
>>> c = "dsf"
>>> li = [1,2,3]
>>> se = {3,2,5,6}
>>> tp = (1,2,3,4)
>>> hash(a)
3
>>> hash(b)
4
>>> hash(c)
8897259870150238697
>>> hash(tp)
485696759010151909
>>> hash(se)
Traceback (most recent call last):
  File "<pyshell#432>", line 1, in <module>
    hash(se)
TypeError: unhashable type: 'set'
>>> hash(li)
Traceback (most recent call last):
  File "<pyshell#433>", line 1, in <module>
    hash(li)
TypeError: unhashable type: 'list'
>>> 

# Извлечь ключ.
>>> dd = {1:"a", 2.:"dsfs", "s":"sffsf", a:"func"}
>>> dd
{1: 'a', 2.0: 'dsfs', 's': 'sffsf', 3: 'func'}
>>> dd[1]
'a'
>>> dd[99]
Traceback (most recent call last):
  File "<pyshell#438>", line 1, in <module>
    dd[99]
KeyError: 99
>>> dd[a]
'func'
>>> dd["s"]
'sffsf'

# ключи + значения tuple.
>>> for k, v in dd.items():
	print(k, ":", v)

	
1 : a
2.0 : dsfs
s : sffsf
3 : func

>>> for tp in dd.items():
	print(tp)

	
(1, 'a')
(2.0, 'dsfs')
('s', 'sffsf')
(3, 'func')
>>> 

# ключи keys.
>>> for k in dd.keys():
	print(k)

	
1
2.0
s
3

# значения values.
>>> for v in dd.values():
	print(v)

	
a
dsfs
sffsf
func

# достать из словаря. если есть индекс и даже если нет.
>>> dd[1]
'a'
>>> dd.get(1)
'a'
>>> dd[999]
Traceback (most recent call last):
  File "<pyshell#463>", line 1, in <module>
    dd[999]
KeyError: 999
>>> dd.get(999)

# добавить/изменить элемент.
>>> dd[0] = 0
>>> dd
{1: 'a', 2.0: 'dsfs', 's': 'sffsf', 3: 'func', 0: 0}


>>> dd[1] = 99  # по индексу - не безопасно.
>>> dd
{1: 99, 2.0: 'dsfs', 's': 'sffsf', 3: 'func', 0: 0}
>>> dd.update({6:66})  # безопасно.
>>> dd.update([(7,77), (8,88), (9,99)])  # безопасно.
>>> dd
{1: 99, 2.0: 'dsfs', 's': 'sffsf', 3: 'func', 0: 0, 6: 66, 7: 77, 8: 88, 9: 99}
>>> 

# удалить элемент.
>>> key = 2.0
>>> dd
{1: 99, 2.0: 'dsfs', 's': 'sffsf', 3: 'func', 0: 0, 6: 66, 7: 77, 8: 88, 9: 99}
>>> if key in dd:
	dd.pop(key)
	print("OK")

	
'dsfs'
OK

>>> if key in dd:
	dd.pop(key)
	print("OK")
else:
	print("nety")

	
nety

# KEYS.
>>> di = {i:i**3 for i in range(50,60)}
>>> di
{50: 125000, 51: 132651, 52: 140608, 53: 148877, 54: 157464, 55: 166375, 56: 175616, 57: 185193, 58: 195112, 59: 205379}
>>> type(di)
<class 'dict'>
>>> di = {i**3 for i in range(50,60)}
>>> di
{140608, 175616, 205379, 166375, 125000, 185193, 195112, 132651, 148877, 157464}
>>> di = {i**3 for i in range(50, 60)}
>>> di
{140608, 175616, 205379, 166375, 125000, 185193, 195112, 132651, 148877, 157464}
>>> type(di)
<class 'set'>
>>> 




