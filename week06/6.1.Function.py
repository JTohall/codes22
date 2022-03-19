# Write a function that prints out a menu of commands we can perform
# Author: Jamie Tohall

def displayMenu ():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) Quit")
    
    choice = input ("Type one letter (a/v/q): ").strip()
    
    return choice
choice  = displayMenu ()
print ("You chose: {}".format(choice))