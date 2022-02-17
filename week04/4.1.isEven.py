# Programme that asks user to input a number, programme will tell if odd or even number
# Author: Jamie Tohall

number = int(input("please enter a number:"))

if (number % 2) == 0:
    print ("{} is an even number.".format(number))

else:
    print("{} is an odd number.".format(number))
