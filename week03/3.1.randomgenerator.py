# Programme will print out a random number between 1 and 10
# Author: Jamie Tohall

import random

# I modified the programme so the user can input the range of numbers
X = int(input("Enter lowest number first: "))
Y = int(input("Now enter your highest number: "))


number = random.randint(X,Y)

print("Your random number is: {}".format(number))