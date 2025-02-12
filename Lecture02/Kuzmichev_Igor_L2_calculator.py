# Kuzmichev_Igor_L2-calculator.

# to write the simple calculator.
# в строке максимум 79 символов!. https://peps.python.org/pep-0008/#maximum-line-length.
# но вопрос - действует ли ограничение-79 на кол-во символов комментария?.
# надо ли безпокоиться о длине комментария или это просто вопрос удобства?.

# Begin.
x = input("x = ")
# 10.
y = input("y = ")
# 20.
x = int(x)
y = int(y)
print('\nResult of maths! + - * /')
print(x, '+', y, '=', x+y)
print(x, '-', y, '=', x-y)
print(x, '*', y, '=', x*y)
print(x, '/', y, '=', x/y)
# 10 + 20 = 30.
# 10 - 20 = -10.
# 10 * 20 = 200.
# 10 / 20 = 0.5.

# Advance.
first_num, second_num = int(input("first_num = ")), int(input("second_num = "))  # в одну строку.
print('\nResult of maths! + - * /')
print(f"{first_num}+{second_num}={first_num+second_num}")  # строка формата f - подстановка значений и вычисление аргументов.
print(f"{first_num}-{second_num}={first_num-second_num}")
print(f"{first_num}*{second_num}={first_num*second_num}")
print(f"{first_num}/{second_num}={first_num/second_num}")
# 10+20=30
# 10-20=-10
# 10*20=200
# 10/20=0.5
