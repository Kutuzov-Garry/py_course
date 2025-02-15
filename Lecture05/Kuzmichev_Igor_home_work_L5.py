# 5.
# HW 5.1 Is leap year.
def is_year_leap(year):
    '''Функция определяет,
    
    является ли год високосным'''
    
    if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


test_data = [1500, 1900, 2000, 2016, 1987]
test_results = [False, False, True, True, False]

for year, result in zip(test_data, test_results):
    if is_year_leap(year) == result:
        print(year, 'is leap? -->', result)
    else:
        print(year, 'from your func -->', \
            is_year_leap(year))
        print('but expected -->', result)

print(is_year_leap.__doc__)
print()


# HW 5.4 Fibonacci numbers.
# Ввод последнего номера последовательности Фибоначчи.
f = int(input("Введите номер позиции \
последовательности Фибоначчи: "))
def febo(n):
    """Функция нахождения определенного
    
    числа Фибоначчи."""
    
    if  n < 1:
        return None
    elif n < 3:
        return 1
    
    f1 = f2 = 1  # Первые два числа Фибоначчи.
    for i in range(3, n+1):  # Цикл начинаем с третьего числа.
        f1, f2 = f2, f1+f2
    
    return f2
    

for i in range(-1, f+1):  # Пришлось поставить +1, почему-то не выводило нужную позицию для просто f.
    print(febo(i))

print(febo.__doc__)
print()
