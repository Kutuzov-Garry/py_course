# Igor, TemperatureConverter and its convert_celsius_to_fahrenheit method.

import xml.etree.ElementTree as ET  # дерево XML.


class TemperatureConverter:  # метод конвертировать Цельсий в Фаренгейт.
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        return 9.0/5.0 * temperature_in_celsius + 32


class ForecastXmlParser:  # XML parsing.
    def __init__(self, temperature_converter):
        self.temperature_converter = temperature_converter

    def parse(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            day = child.find("day").text
            temperature_in_celsius = int(child.find(
                "temperature_in_celsius").text)
            temperature_in_fahrenheit = round(
                self.temperature_converter.convert_celsius_to_fahrenheit(
                    temperature_in_celsius), 1)
            print("{0}: {1} Celsius, {2} Fahrenheit".format(
                day, temperature_in_celsius, temperature_in_fahrenheit))


temperature_converter = TemperatureConverter()
forecast_xml_parser = ForecastXmlParser(temperature_converter)
forecast_xml_parser.parse("forecast.xml")
