# This program tests the function 'calculateDistanceBetweenPoints'
# Its objective: calculate the distance between two points given their coordinates.

import volp0009Library

print("This program calculates the distance between two points given their coordinates")

x1 = float(input("Please inform the position of point A in the X axis > "))
y1 = float(input("Please inform the position of point A in the Y axis > "))
x2 = float(input("Please inform the position of point B in the X axis > "))
y2 = float(input("Please inform the position of point B in the Y axis > "))

distance = volp0009Library.calculateDistanceBetweenPoints(x1,x2,y1,y2)

print("The distance between point A({}x, {}y) and point B({}x, {}y) is equal to {}." .format(x1,y1,x2,y2,distance))