# Continuing from last function, create a programme that continues to display the menu
# until the user picks Q to quit.
# Author: Jamie Tohall

def displayMenu ():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/q): ").strip()
    return choice

def doAdd ():
    print ("In adding")
    
def doView ():
    print ("In Viewing")
    
    
choice  = displayMenu ()

if choice == 'a':
        doAdd() 
elif choice == 'v':
        doView()
elif choice !='q': 
    print ("\n\nPlease select either a, v or q")
    choice = displayMenu()
