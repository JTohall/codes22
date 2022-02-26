# Programme puts 10 random numbers into a queue, then outputs all the values in the queue. Take the
# numbers from the queue one at a time , print it and the current numbers still in the queue.

# Author: Jamie Tohall

import random
queue = []
numberofnumbers = 10 
rangeto = 100
# Programme will generate a queue of ten random numbers between the value of 0 and 100.

for number in range (0, numberofnumbers): 
    queue.append(random.randint(0, rangeto))
    
print ("queue is {}".format(queue))

while len (queue) !=0:
    
    currentnumber = queue.pop(0)
    print ("Current no is {} and the queue is {}".format(currentnumber, queue))
    
print ("The queue is now empty")
