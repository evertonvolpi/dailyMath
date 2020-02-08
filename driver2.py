# This program tests the function 'calculateAreaOfCircle'
# Its objective: calculate the area of a circle given its radius.

import volp0009Library

print("This program calculates the area of a circle given its radius.")

r = float(input("Please inform the radius of the circle > "))

result = volp0009Library.calculateAreaOfCircle(r)

print("The area of a circle of radius '{}' is equal to {}." .format(r,result))