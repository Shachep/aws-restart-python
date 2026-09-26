# Exercise 1: Introducing the string data type
myString = "This is a string."
print(myString)

# Get the data type of the variable using type()
print(type(myString))

# Combine string text with the type function's output converted to a string
print(myString + " is of the data type " + str(type(myString)))


# Exercise 2: Working with string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


# Exercise 3: Working with input strings
name = input("What is your name? ")
print(name)


# Exercise 4: Formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name, color, animal))