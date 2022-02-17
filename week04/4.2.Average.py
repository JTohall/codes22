# Programme will read in rumbers until the user enters 0
# It will then print out the numbers again with their average
# Author: Jamie Tohall

numbers = []

number = int(input("Please enter a number(0 to quit):"))

while number != 0:
    numbers.append(number)
    
    number = int(input("Please enter another number (0 to quit):"))
    
for value in numbers:
    print (value)
    
average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))