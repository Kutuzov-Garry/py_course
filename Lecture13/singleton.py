# singleton.py.

class Dog:
    inst_cont = False
    def __init__(self, name):
        if Dog.inst_cont == False:
            self.name = name
            Dog.inst_cont = True
        else:
            raise Exception("собака - это синглтон.")

Dog.inst_cont
False
# не содержится Экземпляр.

d1 = Dog("Bobik")

Dog.inst_cont
False
d1 = Dog("Bobik")
Dog.inst_cont
True
d1.name
'Bobik'
d2 = Dog("Vasia")
Traceback (most recent call last):
  File "<pyshell#858>", line 1, in <module>
    d2 = Dog("Vasia")
  File "<pyshell#853>", line 8, in __init__
    raise Exception("собака - это синглтон.")
Exception: собака - это синглтон.


class PersonID:
    inst_cont = False
    def __init__(self, name):
        if PersonID.inst_cont == False:
            self.name = name
            self.pers_id = 12345
            PersonID.inst_cont = True
        else:
            raise Exception("Person - это синглтон.")
