# Igor L10 - main.
from mobile_phone_class import MyMobile

phone1 = MyMobile("37529111")  # Присвоить number для Класса.
phone2 = MyMobile("37533222")
print("phone1:", phone1.number)
print("phone2:", phone2.number)

def main():

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
                        print(phone.call(cally))
                else:
                        print("Выбран несуществующий пункт")

if __name__ == "__main__":
    print("main.py has been started")
    main()
