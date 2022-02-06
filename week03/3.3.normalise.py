# Programme will read in a string and strips any leading/trailing spaces
# The programme should also convert the string to lower case and output the 
# length of the input and output strings.
# Author: Jamie Tohall

rawString = input("Please enter a string:")
normalisedstring = rawString.strip().lower()

LengthofRawString = len (rawString)
LengthofNormalised = len (normalisedstring)

print("That string normalised is:{}".format(normalisedstring))
print("We reduced the input string from {} to {} characters".format(LengthofRawString, LengthofNormalised))