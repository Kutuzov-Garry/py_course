# Igor L10 - test_mobile_phone (без модулей).

class MyMobile:
        """Класс, представляющий мобильный телефон\n"""
        def __init__(self, number):
                self.number = number
                self.switch = False
        def turn_on(self):
                self.switch = True
                print(self.switch)        
                return f"mobile phone {self.number} is enabled"
        def turn_off(self):
                self.switch = False
                print(self.switch)
                return f"mobile phone {self.number} is turned off"
        def call(self):
                print(self.switch)
                if self.switch == True:
                        return f"calling {cally}"
                return f"mobile phone {self.number} is turn off now"

print(MyMobile.__doc__)


phone1 = MyMobile("37529111")  # Присвоить number для Класса.
phone2 = MyMobile("37533222")
print("phone1:", phone1.number)
print("phone2:", phone2.number)

while True:
        choice = input("Выберите телефон 1 или 2: ")
        if choice == "1":
                phone = phone1
        else:
                phone = phone2

        action = input("\nВыберите действие:\n1 - вкл.тел,\n2 - выкл.тел,\n3 - позвонить\n")

        if action == "1":
                print(phone.turn_on())
        elif action == "2":
                print(phone.turn_off())
        elif action == "3":
                cally = input("Введите номер для набора: ")
                print(phone.call())
        else:
                print("Выбран несуществующий пункт")
