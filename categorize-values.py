# Creating a mixed-type list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Iterating through the list to print items and their data types
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))