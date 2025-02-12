# Home work 3.1.
# Работа со списком.
hat_list = [1,2,3,4,5]
print("Вот исходный список:", hat_list)
print("Длина списка:", len(hat_list))  # Степ 0. Длина списка.
mid = input('Введите целочисленный номер, которым заменим средний номер в списке: ')
print("Вы ввели:", mid)
hat_list.pop(2)  # Удалить индекс-2.
hat_list.insert(2, mid)  # Степ 1. Вставить индекс-2 значением пользователя.
print("Теперь список таков:", hat_list)
hat_list.pop()  # Степ 2. Удалит последний индекс списка.
print("Удалили последний элемент списка. Теперь список таков:", hat_list)
print("Длина списка:", len(hat_list))  # Степ 3. Длина списка.
print()

# Home work 3.3.
# Bubble sort.
li = [3, 5, 2, 0, -99, -25, 97]
swap = True  # Ключ остановки цикла.
print('Исходный список:', li)

while swap:
    swap = False  # Сброс Ключа остановки цикла.
    for i in range(len(li)-1):  # Для индексов списка от нулевого до предпоследнего.
        if li[i] > li[i+1]:  # Сравнить два соседних индекса.
            li[i], li[i+1] = li[i+1], li[i]  # Заменить их местами.
            swap = True  # Восстановить Ключ остановки цикла для продолжения цикла.

print('Итоговый список:', li)
print()

# Home work3.5 split().
li = [int(value) for value in input('Введите до пяти чисел через пробел:').split()]
print(li)
print("Сумма:", sum(li))
print()

# https://docs.python.org/3/library/functions.html.
