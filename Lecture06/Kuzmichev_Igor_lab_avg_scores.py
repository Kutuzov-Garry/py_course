# 6.1. Kuzmichev_Igor_lab_avg_release.py.
school_class = {}

menu = """
1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход
"""
print()
oper = int(input(menu))

while oper != -1:
    if oper == 1:
        name = input("name:")
        if name not in school_class:
            school_class[name] = ()
            print("Студент успешно добавлен сейчас.")
        else:
            print("Уже был создан.")
    elif oper == 2:
        name = input("name:")
        if name in school_class:
            grade = int(input("grade (1-10):"))
            school_class[name] += (grade, )
            print("Оценка успешно добавлена сейчас.")
        else:
            print("Студента пока нет в списке.")
    elif oper == 3:
        if len(school_class) < 1:
            print("Оценок пока нет.")
        elif len(school_class) >= 1:
            for name in school_class.keys():
                grades = school_class[name]
                if len(grades) >= 1:
                    print(name)
                    print(school_class[name])
                    print("Средний балл:")
                    print(sum(grades)/len(grades))
                else:
                    print("У", name, "пока нет оценок.")
    oper = int(input(menu))
