# Kuzmichev_Igor_class_work_L3.py.

# Lists.
>>> numbers = []

>>> li = []
>>> li1 = list()
>>> print(li)
[]
>>> print(li1)
[]

# Add a new list.
>>> a = [1,2,3,True, "edfe"]
>>> a
[1, 2, 3, True, 'edfe']
>>> a[3]
True
>>> a["1"]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a["1"]
TypeError: list indices must be integers or slices, not str
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a[5]
IndexError: list index out of range
>>> type(li)
<class 'list'>
>>> type(a)
<class 'list'>
>>> type(a[0])
<class 'int'>

# List methods.
>>> st = "Hello"
>>> st.upper()  # ЗАГЛАВНЫЕ.
'HELLO'
>>> q = 100
>>> q.upper()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    q.upper()
AttributeError: 'int' object has no attribute 'upper'
>>> a.upper()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> "asd".upper()  # ЗАГЛАВНЫЕ сразу для переменной.
'ASD'

>>> a = [4,3,45,6,7,8,93]
>>> a
[4, 3, 45, 6, 7, 8, 93]
>>> a.append(777)  # Добавить в конец листа.
>>> a
[4, 3, 45, 6, 7, 8, 93, 777]
>>> a.insert(2,9)  # Вставить число 9 в индекс 2 (третья позиция с начала списка) со сдвигом вправо остальных индексов.
>>> a
[4, 3, 9, 45, 6, 7, 8, 93, 777]
>>> len(a)  # Длина списка.
9
>>> a.reverse()  # Перевернуть список концом в начало.
>>> a
[777, 93, 8, 7, 6, 45, 9, 3, 4]
>>> a.reverse()  # Перевернуть список концом в начало - привели список в исходное состояние.
>>> a
[4, 3, 9, 45, 6, 7, 8, 93, 777]
>>> 
>>> a.pop()  # Удалить последний индекс списка.
777
>>> a
[4, 3, 9, 45, 6, 7, 8, 93]
>>> res = a.pop(3)  # Удалить третий (начиная с нуля - четвёртый по счету с начала) индекс списка.
>>> a
[4, 3, 9, 6, 7, 8, 93]
>>> del a[0]  # Удалить нулевой индекс.
>>> a
[3, 9, 6, 7, 8, 93]
>>> li
[]
>>> del li  # Удалить список.
>>> li
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    li
NameError: name 'li' is not defined
>>> 
>>> a
[3, 9, 6, 7, 8, 93]
>>> a.remove(1)  # Попытка удалить число 1, которого нет в списке.
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
>>> a.remove(8)  # Удаляем 8 из списка.
>>> a
[3, 9, 6, 7, 93]


>>> toDel = 555
>>> if toDel in a:
	a.remove(toDel)

# Считаем количество одинаковых чисел в списке.
>>> a.count(6)
1
>>> a.append(6)
>>> a.count(6)
2
>>> a.count(777)
0
>>> a.clear()  # Очистить список.
>>> a
[]  # Список опустел.
>>> a = [3, 9, 45, 6, 7, 93, 6]
>>> a.index(6)  # Какой индекс у первого числа 6 в списке?.
3
>>> a.index(6, a.index(6)+1)  # Какой индекс у следующего числа 6 в списке?.
6
>>> a
[3, 9, 45, 6, 7, 93, 6]
>>> li = [7,7,7]
>>> a += li  # К списку 'a' в хвост прибавить список 'li'.
>>> a
[3, 9, 45, 6, 7, 93, 6, 7, 7, 7]
>>> a *= 2  # Удвоить список.
>>> a
[3, 9, 45, 6, 7, 93, 6, 7, 7, 7, 3, 9, 45, 6, 7, 93, 6, 7, 7, 7]
>>> 

>>> q = [1,3,5,7,2,4,6]
>>> q
[1, 3, 5, 7, 2, 4, 6]
>>> q[0]  # Индекс 0.
1
>>> q[6]  # Индекс 6.
6
>>> q[-1]  # Последний индекс (хвост).
6
>>> q[-7]  # Седьмой с конца индекс.
1
>>> q
[1, 3, 5, 7, 2, 4, 6]
>>> q[2] = 555  # Заменить второй индекс на новое значение.
>>> q
[1, 3, 555, 7, 2, 4, 6]
>>> q[3] = 999  # Заменить третий индекс на новое значение.
>>> q
[1, 3, 555, 999, 2, 4, 6]
>>> 

# Цикл для вывода списка.
>>> for i in q:
	print(i)

	
1
3
555
999
2
4
6


>>> li = []
>>> for i in range(len(li)):
	print()
	print(li[i])

# Манипуляции со списком.
>>> li = [44,55,66,777]
>>> li
[44, 55, 66, 777]
>>> li.reverse()  # Перевернуть.
>>> li
[777, 66, 55, 44]
>>> li.append(1000)  # Добавить индекс в хвост.
>>> print(li)
[777, 66, 55, 44, 1000]
>>> sorted(li)  # Сортинг по возрастанию, без изменения самого списка.
[44, 55, 66, 777, 1000]
>>> li  # Список неизменен.
[777, 66, 55, 44, 1000]

>>> for i in sorted(li):  # Сортинг по возрастанию, по вертикали.
	print(i, sep=" ")

	
44
55
66
777
1000
>>> for i in sorted(li):
	print(i, end=" ")

	
44 55 66 777 1000  # Сортинг по возрастанию, в строку.
>>> li
[777, 66, 55, 44, 1000]
>>> sorted(li, reverse=True)
[1000, 777, 66, 55, 44]
>>> li
[777, 66, 55, 44, 1000]
 

>>> # Lab 3.2. по желанию.


>>> li = [3, 5, 0, -10, 4] # Bubble.
>>> a, b = 66, 77
>>> tmp = a
>>> a = b
>>> b = tmp
>>> a
77
>>> b
66
>>> a, b = 66, 77
>>> a = b
>>> b = tmp
>>> a
77
>>> b
66
>>> a, b = 66, 77
>>> a, b = b, a
>>> a
77
>>> b
66
>>> # Поменять местами значения переменных.
>>> li = [3, 5, 0, -10, 4]
>>> li [1], li[2] = li[2], li[1]
>>> li
[3, 0, 5, -10, 4]
>>> 
>>> 
>>> li [2], li[3] = li[3], li[2]
>>> li
[3, 0, -10, 5, 4]
>>> li [3], li[4] = li[4], li[3]
>>> li
[3, 0, -10, 4, 5]

>>> # Имитация работы bubble sort.
>>> li
[3, 0, -10, 4, 5]
>>> max(li)
5
>>> min(li)
-10
>>> sum(li)
2
>>> sum(li)/len(li)
0.4
>>> print
<built-in function print>
>>> max
<built-in function max>
>>> # Определение индекса по свойству.
>>> 
>>> # Можно гуглить.>>> 
>>> # https://docs.python.org/3/library/functions.html.
>>> 


>>> li = [1,2,3,4]
>>> a = li
>>> li
[1, 2, 3, 4]
>>> a
[1, 2, 3, 4]
>>> id(li)
1497709883016
>>> id(a)
1497709883016
>>> a[1] = 99999
>>> a
[1, 99999, 3, 4]
>>> li
[1, 99999, 3, 4]
>>> a = li.copy()
>>> a
[1, 99999, 3, 4]
>>> li
[1, 99999, 3, 4]
>>> id(li)
1497709883016
>>> a = li[:]  #
>>> 
>>> 
>>> 
>>> li
[1, 99999, 3, 4]
>>> li = [1,2,3,4]
>>> li
[1, 2, 3, 4]
>>> li[:]
[1, 2, 3, 4]
>>> li[:3]
[1, 2, 3]
>>> li += li
>>> li
[1, 2, 3, 4, 1, 2, 3, 4]

>>> kk = li[::2]  # Перешагивать по 2.
>>> kk
[1, 3, 1, 3]
>>> 
>>> li
[1, 2, 3, 4, 1, 2, 3, 4]

>>> li[::-1]  # Разворот списка.
[4, 3, 2, 1, 4, 3, 2, 1]

>>> # Проверка есть ли число в списке.
>>> 777 in li
False
>>> 
>>> 4 in li
True
>>> 


>>> # SET TYPE.
>>> 
>>> myset = set()
>>> type(myset)
<class 'set'>
>>> 
>>> s = {}
>>> type(s)
<class 'dict'>
>>> s = set()
>>> type(s)
<class 'set'>

>>> s = {"df", 1, 2, 3, 1, 1, 2, 3}
>>> s
{1, 2, 3, 'df'}
>>> s.add(1)  # Не добавился дублирующий элемент.
>>> s
{1, 2, 3, 'df'}
>>> 
>>> for v in s:
	print(v, end=" ")

	
1 2 3 df

>>> # Проверить что есть в Списке.
>>> 999 in s
False
>>> 1 in s
True

>>> # Добавка уникальных элементов.
>>> s.update({1,2,3,4,6666})
>>> s
{1, 2, 3, 4, 6666, 'df'}

>>> s
{1, 2, 3, 4, 6666, 'df'}
>>> s.clear()  # Чистим список.
>>> s

set()
>>> s = {1,2,3,4, 666, "df"}
>>> s.remove(555)  # Нечего удалить.
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    s.remove(555)
KeyError: 555

>>> s
{1, 2, 3, 4, 666, 'df'}
>>> s.discard(444)  # Не ругается, если нет такого элемента.
>>> 
>>> s.discard(2)  # Удаляем 2, т.к. она есть в списке.
>>> s
{1, 3, 4, 666, 'df'}
>>> len(s)  # Длина списка.
5

>>> li
[1, 2, 3, 4, 1, 2, 3, 4]
>>> li = list(set(li))  
>>> li
[1, 2, 3, 4]
>>> 
>>> S
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> S
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> s
{1, 3, 4, 666, 'df'}
>>> st
'Hello'
>>> list(st)
['H', 'e', 'l', 'l', 'o']
>>> set(st)  # Привели к уникальности элементов.
{'l', 'e', 'o', 'H'}
>>> 
>>> 
>>> int(li)
Traceback (most recent call last):
  File "<pyshell#285>", line 1, in <module>
    int(li)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> 
>>> 
>>> # print печатает СТРОКУ!.
>>> print(li)
[1, 2, 3, 4]
>>> ppp = str(li)  # Перевели в строчное.
>>> ppp
'[1, 2, 3, 4]'
>>> list(ppp)  # Обратно из строчной нет возврата.
['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ']']
>>> 
>>> 
>>> # Test.
>>> my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
>>> set(my_list)
{1, 2, 4, 6, 9}
>>> my_list
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
>>> my_list[::-1]  # Список в обратном порядке.
[9, 2, 6, 2, 4, 1, 4, 4, 2, 1]
>>> print(my_list)
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
>>> li2 = my_list[::-1]  # Сохранить обратку в другой лист.
>>> li2
[9, 2, 6, 2, 4, 1, 4, 4, 2, 1]
>>> 
>>> # List comprehention.
>>> li = [1,2,3,4,5]
>>> resList = []
>>> for v in li:
	resList.append(v**2)

# Работа с итемами списка через цикл, в одну строку.
>>> li
[1, 2, 3, 4, 5]
>>> resList
[1, 4, 9, 16, 25]
>>> li = [1,2,3,4,5]
>>> resList = [v**2 for v in li]
>>> resList
[1, 4, 9, 16, 25]
>>> li = [1,2,3,4,5,6,7,8,9,10]
>>> resList
[1, 4, 9, 16, 25]
>>> 

>>> numbers = [int(input("-->")) for i in range(int(input("n-->")))]
n-->6  # Сколько юзер хочет ввести чисел?.
-->44
-->55
-->66
-->1
-->2
-->3
>>> numbers
[44, 55, 66, 1, 2, 3]
>>> 


>> # List in list.
>>> li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> li = [1,2,3,4]
>>> li[0]
1
>>> li = [[], [], []]
>>> li[0]
[]
>>> li[-1]
[]
>>> li = [[1,2,3], [11,22,33], [0,5,8]]
>>> li[0]
[1, 2, 3]
>>> li[1]
[11, 22, 33]
>>> li[2]
[0, 5, 8]
>>> li[0] [2]
3
>>> li[1] [1]
22
>>> li[2] [0]
0
>>> li[0].append(333)
>>> li
[[1, 2, 3, 333], [11, 22, 33], [0, 5, 8]]
>>> # Добавили 333 в 0й список.
>>> 
>>> li[0] [2] = 222
>>> li
[[1, 2, 222, 333], [11, 22, 33], [0, 5, 8]]
>>> # Добавили 333 в 0й список в индекс-2.

# Пробежали по тестам по Лекция-1.
