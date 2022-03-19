# No work on reading in the modules for the programme
# Author: Jamie Tohall

students= []
def readModules ():
    return []

def doAdd (students):
    currentstudent = {}
    currentstudent ["name"]=input("Enter a name: ")
    currentstudent ["modules"]= readModules ()
    students.append(currentstudent)
    
doAdd (students)
doAdd (students)
print (students)
    

def readModules ():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit)").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit)").strip()
    return modules