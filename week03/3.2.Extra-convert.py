# Takes in a float amount in dollars and returns the absolute amount in cent
# Author: Jamie Tohall

dollars = float(input("Enter amount of dollars:"))
cent = abs (dollars*100) 

print ("That amount in cent is {}".format(cent))