# Programme will print out a random fruit
# Author: Jamie Tohall

import random

fruits = ['Banana', 'Orange', 'Strawberry', 'Grapes', 'Apple']

index = random.randint (0,len(fruits)-1)

fruit = fruits[index]
print ("Your random fruit is: {} " .format(fruit))
