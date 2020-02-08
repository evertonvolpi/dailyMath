import math

#This function calculates the area of a circle from its radius.
# The user will inform: 'radius'.
def calculateAreaOfCircle(radius):
    area = round((math.pi * radius ** 2), 2)
    return(area)


#This function calculates the MPG (Miles Per Gallon) of a car.
# The user will inform: 'miles' driven and 'gallons' consumed.
def calculateMpg(miles,gallons):
    mpg = round((miles / gallons),2)
    return(mpg)


# This function makes the temperature conversion from Fahrenheit to Celcius.
# The user will inform: temperature in 'fahrenheit'.
def convertFahrenheitToCelcius(fahrenheit):
    celcius = round(((fahrenheit - 32) * 5 / 9), 2)
    return(celcius)


# This program calculates the distance between two points given their coordinates.
# The user will inform: Point A in axis 'x1' and 'y1; point B in axis 'x2' and 'y2'.
def calculateDistanceBetweenPoints(x1,x2,y1,y2):
    distance = round(math.sqrt(((x2 - x1)**2)+((y2 - y1)**2)),2)
    return(distance)