# Igor phone accu temperature.

import logging
import random

FORMAT = '%(levelname)s - %(message)s'  # формат вывода логируемых данных.

class BatterySimulation:
    '''программа логирования температуры аккумулятора мобильного
    телефона за 1 час с выборкой каждую 1 минуту'''
    def __init__(self, logger):
        self.logger = logger

    def simulate_last_hour(self):
        for minute in range(1, 60 + 1):  # 60 значений с шагом 1 минута.
            temperature = random.randint(20, 40)  # вызов рандомных значений в рамках 20-40 C".

            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >= 30 and temperature <= 35:
                self.logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception("Temperature is out of range!")

logger = logging.getLogger("battery.temperature")

# вывод в указанных файл лога в режиме перезапись.
handler = logging.FileHandler("battery_temperature.log", mode="w")
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

battery_simulation = BatterySimulation(logger)
battery_simulation.simulate_last_hour()  # вызов функции получения и логирования температуры.
