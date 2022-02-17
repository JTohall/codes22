# Programme will ask user to guess a number and also let them know if thier guess was too high or low
# Author: Jamie Tohall

numbertoguess = 66

guess = int(input("Guess a number: "))
while guess != numbertoguess:
    if guess < numbertoguess: print ("Too Low")
    
    else: print("Too High")
    guess = int(input("Please guess again: "))
    
print ("Well done! The correct number is",numbertoguess)
