# All previous functions 
# Author: Jamie Tohall

def displayMenu ():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/q): ").strip()
    return choice

def doAdd (students):
    currentstudent = {}
    currentstudent ["name"]=input("Enter a name: ")
    currentstudent ["modules"]= readModules ()
    students.append(currentstudent)
    
def readModules ():
    modules = []
    moduleName = input("\t\t Enter the first module name (blank to quit): ").strip()
        
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        module["grade"]=int(input("\t\t Enter grade: "))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit)").strip()
        
    return modules

      
students = []
choice = displayMenu()
while(choice != 'q'):
    
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q: ")
        
    choice=displayMenu()
    
def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);
        
def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"])) 
