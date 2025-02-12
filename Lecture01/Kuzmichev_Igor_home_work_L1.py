# Домашняя работа Лекция 1.

# Home work 1.0.
print("Hello, World!")  # просто вывести текст.
print()

# Home work 1.1.
print("Programming", "Essentials", "in", sep="***", end="...Python")  # sep and end.
print()

# Home work 1.2.
print()  # отступ.
print("    *")  # рисунок стрелка вверх.
print("   * *")
print("  *   *")
print(" *     *")
print("**** ****")
print("   * *")  # сузить ножку стрелки.
print("   * *")
print("   ***")
print()

# Home work 1.3.
print('"I\'m"\n""Learning""\n"""Python"""')  # вывести три строки одну под одной.
print()
      
 # Home work 1.4.
john = 2  # create the variables equal to the numbers of fruit possessed.
mary = 4
adam = 6
total_apples = john + mary + adam  # объединяем три начальных переменных в одну новую.
print("total_apples are", total_apples)
print()

# Home work 1.5.
kilometers = 12.25  # сколько километров дано.
miles = 7.38  # сколько миль дано.
kilometers_to_miles = (kilometers / 1.61)  # переводим км в мили.
miles_to_kilometers = (miles * 1.61)  # переводим мили в км.
print(kilometers, "kilometers is ", round(kilometers_to_miles, 2), "miles")  # столько км это столько миль.
print(miles, "miles is ", round(miles_to_kilometers, 2), "kilometers")  # столько миль это столько км.
print()
print(kilometers, "kilometers is ", round(kilometers / 1.61, 2), "miles")  # второй способ без доп переменных.
print(miles, "miles is ", round(miles * 1.61, 2), end=" kilometers")  # второй способ без доп переменных.

