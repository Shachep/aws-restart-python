userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply.lower() == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    userReply = input("Would you like to buy stamps, buy an envelope, or copy a document? (Enter stamps, envelope, or copy) ")

if userReply.lower() == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply.lower() == "envelope":
    print("We have many sizes of envelopes to choose from.")
elif userReply.lower() == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are your {} copies.".format(copies))
else:
    print("Thank you, please come again.")