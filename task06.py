# 6. Create a class named TemperatureConverter. Then make two methods :
#  A. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
#  B. convertFahrenheit - It will take celsius and will print it into Fahrenheit.

class TemperatureConverter:
    def convert_celsius(self):
        f = int(input('Enter the temperature in Fahrenheit: '))
        c = round((f - 32) * (5/9), 3)
        print(f'{f}{chr(176)}F = {c}{chr(176)}C')

    def convert_fahrenheit(self):
        c = int(input('Enter the temperature in Celsius: '))
        f = round((c * 9/5) + 32, 3)
        print(f'{c}{chr(176)}C = {f}{chr(176)}F')


key = int(input('1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\nEnter your choice: '))
obj1 = TemperatureConverter()
if key == 1:
    obj1.convert_celsius()
if key == 2:
    obj1.convert_fahrenheit()
