# This program tests the function 'convertFahrenheitToCelcius'
# Its objective: convert the temperature value from Fahrenheit to Celcius.

import volp0009Library

print("This program makes the temperature conversion from Fahrenheit to Celcius.")

fahrenheit = float(input("Please inform the temperature in Fahrenheit > "))

celcius = volp0009Library.convertFahrenheitToCelcius(fahrenheit)

print("{} Fahrenheit is equal to {} Celcius." .format(fahrenheit,celcius))