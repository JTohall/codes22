# Create a tuple that stores the months of the year, from that tuple create another tuple with
# just the summer months (May, June, July), print out summer months one at a time.

#Author: Jamie Tohall

# create tuple of all the 12 months in the year 
months = ("January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December")

# Define summer months as the 5th, 6th & 7th month in the year 
Summer = months [4:7]

# Use 'for' to iterate the summer months
for months in Summer:
    print (months) # Should print May, June and July in list form