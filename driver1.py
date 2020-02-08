# This program tests the function 'calculateMpg'
# Its objective: calculate the MPG-Miles Per Gallon of a car.

import volp0009Library

print("This program calculates the MPG-Miles Per Gallon of a car.")

miles = float(input("Please inform how many miles you have driven > "))
gallons = float(input("Please inform how many gallons you have used > "))

mpg = volp0009Library.calculateMpg(miles,gallons)

print("The MGP of a car that consumed {} gallons in {} miles is equal to {}." .format(gallons,miles,mpg))