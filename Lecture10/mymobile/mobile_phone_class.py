# Igor L10 - mobile_phone_class.

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
        def call(self, cally):
                self.cally = cally
                print(self.switch)
                if self.switch == True:
                        return f"calling {self.cally}"
                return f"mobile phone {self.number} is turn off now"

print(MyMobile.__doc__)
