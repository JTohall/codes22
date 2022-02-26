# Programme stores a student name and a list of their courses and grades in a dict. The programme 
# should then print out their data

# Author: Jamie Tohall

student = {"name" : "Mary", 
"modules" : [{"coursename":"Programming", "grade" : 45}, 
{"coursename":"history", "grade" : 99}]}


print ("student: {}".format(student["name"]))

for module in student ["modules"]: 
    print ("\t {} \t: {}".format(module["coursename"],module["grade"]))
    