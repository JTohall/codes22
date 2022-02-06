# Programme will read in two numbers and divide the first number by the second, gives the integer result and the remainder
# Author: Jamie Tohall

X = int(input("Enter first number:"))
Y = int(input("Enter the number you want to divide by:"))

answer = int (X//Y) 
# Will give the int division

remainder = (X%Y)
# Will give the remainder

print("{} divided by {} is: {} with remainder: {}" .format (X, Y, answer, remainder))