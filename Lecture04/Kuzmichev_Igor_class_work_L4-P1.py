# Kuzmichev_Igor_class_work_L4

А  про гит можете почитать вот это:
https://www.atlassian.com/ru/git/tutorials/what-is-git
Atlassian
Что такое Git? | Atlassian Git Tutorial

# Git — это развитая система контроля версий с активной поддержкой и открытым исходным кодом,.
# которую используют тысячи разработчиков из разных точек мира.

>>> a = [1, 999, 3, 444]
>>> a = [1, 999, 3, 4]
>>> a
[1, 999, 3, 4]
>>> gg = a.copy()
>>> gg
[1, 999, 3, 4]
>>> gg[1] = 777
>>> a
[1, 999, 3, 4]
>>> lit = [1,2,3]
>>> a = [22, lit, 33, 44]
>>> a
[22, [1, 2, 3], 33, 44]
>>> bb = a[:]
>>> bb
[22, [1, 2, 3], 33, 44]
>>> lit[2] = 999
>>> lit
[1, 2, 999]
>>> a
[22, [1, 2, 999], 33, 44]
>>> bb
[22, [1, 2, 999], 33, 44]
>>> cc = a.copy()
>>> a
[22, [1, 2, 999], 33, 44]
>>> bb
[22, [1, 2, 999], 33, 44]
>>> cc
[22, [1, 2, 999], 33, 44]
>>> import copy
>>> dd = copy.deepcopy(a)
>>> dd
[22, [1, 2, 999], 33, 44]
>>> lit[1] = 333
>>> dd
[22, [1, 2, 999], 33, 44]
>>> cc
[22, [1, 333, 999], 33, 44]
>>> # deepcopy - Питон не будет копировать вложенности.

# Python поддерживает UTF-8.
>>> имя = "Джонни"
>>> print(имя)

Джонни


>>> li = [1,2,3]
>>> li[1] = 88
>>> li
[1, 88, 3]
>>> a = 88
>>> a = 33
>>> st = "12345"
>>> st
'12345'
>>> st[0]
'1'
>>> st[0] = "kjsdfiof"
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    st[0] = "kjsdfiof"
TypeError: 'str' object does not support item assignment

>>> li
['Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ', 'Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ď', 'ď', 'Đ', 'đ', 'Ē']
>>> for char in li:
	print(ord(char)), end=" ")
	
SyntaxError: invalid syntax
>>> for char in li:
	print(ord(char), end=" ")

	
205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274

>>> # Доступ к элементам строки по индексам.
>>> for i in range(len(st))
SyntaxError: invalid syntax
>>> for i in range(len(st)):
	print("index:", i, "| value:"), st[i])
	
SyntaxError: invalid syntax
>>> for i in range(len(st)):
	print("index:", i, "| value:", st[i])

	
index: 0 | value: 1
index: 1 | value: 2
index: 2 | value: 3
index: 3 | value: 4
index: 4 | value: 5
>>> 

>>> # Шифр Цезаря.
>>> msg = "rome: grog, shakira."
>>> secret = 8
>>> secretMessage = ""
>>> for char in msg:
	secretMessage += chr(ord(char)+secret)

	
>>> secretMessage
'zwumB(ozwo4({pisqzi6'
>>> msg
'rome: grog, shakira.'
>>> result = ""
>>> for char in secretMessage:
	result += chr(ord(char)-secret)

	
>>> result
'rome: grog, shakira.'
>>> # Дешифровали.

>>> 
>>> 
>>> st
'12345'
>>> st[::-1]
'54321'
>>> st
'12345'
>>> st = 'hellohshsh'
>>> st
'hellohshsh'
>>> st = "[fix] dssjd"
>>> st[1:4]
'fix'
>>> # Извлечь индексы из списка.
>>> 
>>> st[2:]
'ix] dssjd'
>>> st[::3]
'[xdj'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s = 'qwerty'
>>> s
'qwerty'
>>> s.upper()
'QWERTY'
>>> s
'qwerty'
>>> v = 'ASDFG'
>>> v.lower()
'asdfg'
>>> v
'ASDFG'
>>> 
>>> 
>>> st
'[fix] dssjd'
>>> name = input("->").upper()
->ajdasf
>>> name
'AJDASF'
>>> 
>>> 
>>> s.index("t")
4
>>> # Найти символ по индексу.
>>> 
>>> name = "John"
>>> name[:2]+"K"+name[3:]
'JoKn'
>>> # Поменять определенный индекс.
>>> 
>>> name = "gggggggklkwpggglkg"
>>> name.count("g")
11
>>> name.count("!")
0
>>> name.isalpha()
True
>>> name = "gggggggklkwpggglkg1"
>>> name.isalpha() # Только буквы?.
False
>>> numbers = "12345"
>>> numbers.isdigit()
True
>>> # Только цифры.




