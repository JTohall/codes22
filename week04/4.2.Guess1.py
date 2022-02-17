# Programme asks user to guess a number and will keep prompting user until right number is guessed
# Author: Jamie Tohall

numbertoguess = 66

guess = int(input("Guess a number:"))

while guess != numbertoguess:
    print ("wrong!")
    guess = int(input("Please guess again:"))
    
print ("Correct! Well Done! The right number is",format(numbertoguess))
