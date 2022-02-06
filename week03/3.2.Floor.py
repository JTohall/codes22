# Programme floors a number
# Takes in a float and outputs an int rounded down
# Author: Jamie Tohall

import math

numbertofloor = float(input("Enter a float number: "))
floorednumber = math.floor(numbertofloor)

print ('{} floored is {}'.format(numbertofloor, floorednumber))