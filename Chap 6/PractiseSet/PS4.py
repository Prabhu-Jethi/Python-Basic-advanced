## Find out whether a given username contains less than 10 characters or not.

username = input("Enter your name: ")

if (len(username)<10):
    print("Your username has less than 10 characters")
else:
    print("Your username contains more than 10 characters")