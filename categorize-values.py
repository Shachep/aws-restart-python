# Creating a mixed-type list
myMixedTypeList = [45, 29057, 1.5, True, "My dog is on the bed.", "45"]

# Using a for loop to iterate through the list and print each item's data type
for item in myMixedTypeList:
    print(f"Item: {item} | Data Type: {type(item)}")