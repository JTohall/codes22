# Programme will ask user to enter their percentage mark and will output their grade
# Author: Jamie Tohall

percentage = float(input("Enter the percentage:"))

if percentage < 40: print("Fail")

elif percentage <50: print ("Pass")

elif percentage <60: print ("Merit 2")

elif percentage <70: print ("Merit 1")

else: print("Distinction")
