# Home work 2.1 p.27.
# Вариант-1
# Запросить ввести четыре числа.
num1 = int(input("Введите первое число из четырёх: "))
num2 = int(input("Введите второе число из четырёх: "))
num3 = int(input("Введите третье число из четырёх: "))
num4 = int(input("Введите четвёртое число из четырёх: "))
# Сравнение первой пары первого ряда и определение large_num11.
if num1 > num2:
    large_num11 = num1
    print("large_num11 is", large_num11)
else:
    large_num11 = num2
    print("large_num11 is", large_num11)

# Сравнение второй пары первого ряда и определение large_num12.  
if num3 > num4:
    large_num12 = num3
    print("large_num12 is", large_num12)
else:
    large_num12 = num4
    print("large_num12 is", large_num12)

# Сравнение первой пары второго ряда и определение large_num21.
if large_num11 > large_num12:
    large_num21 = large_num11
    print("large_num21 is", large_num21)
else:
    large_num21 = large_num12
    print("large_num21 is", large_num21)
print()

# Home work 2.4 p.45.
# Детская считалка до пяти ).
import time
for i in range(1, 6):
    print("Mississippi", i)
    time.sleep(1)
    
print("Final")
print()

# Home work 2.6 p.67.
# Operation.
operation = input('Выберите операцию +-*/ or exit: ')

# Цикл для операции и ввод двух переменных.
while operation != 'exit':
    num1, num2 = int(input('Введите 1е число: ')), int(
        input('Введите 2е число: '))
    
    if operation == "+":
        print("сумма =", num1 + num2)
    elif operation == "-":
        print("разность =", num1 - num2)
    elif operation == "*":
        print("произведение =", num1 * num2)
    elif operation == "/":
        print("частное =", num1 / num2)
    else:
        print(f'Указанное значение не определено!--> {operation}')  # Введена недопустимая операция.

print("Вы ввели exit")
