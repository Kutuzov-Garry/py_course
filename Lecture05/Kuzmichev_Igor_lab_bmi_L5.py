# 5.

# BMI.
print("Предлагаем узнать свой ИМТ (Индекс массы тела). \
    \nЗначения от 11 до 18 считаются Дефицитом, \
    \nЗначения от 18 до 25 считаются Нормой, \
    \nЗначения от 25 до 30 считаются Предожирением.")


def bmi(weight, height):
    """Функция расчёта ИМТ (Индекс массы тела)
    по указанию веса и роста."""
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return round((weight / height ** 2), 1)  # Вычисление ИМТ и округление до 1 цифры после запятой.

print()
weight = int(input("Укажите вес в целых кг, например 81: "))
height = float(input("Укажите рост в м.см, например 1.84: "))

print("ИМТ = ", bmi(weight, height))

print()
print("Примеры:")
print("вес 81, рост 1.84")
print("вес 65, рост 1.75")
print(bmi(81, 1.84))
print(bmi(65, 1.75))

print()
print(bmi.__doc__)
