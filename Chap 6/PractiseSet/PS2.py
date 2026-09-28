## Find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take these spams.

mark1 = int(input("Enter Marks 1: "))
mark2 = int(input("Enter Marks 2: "))
mark3 = int(input("Enter Marks 3: "))

total_percentage = (100 * (mark1 + mark2 + mark3))/100

if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You are passed:", total_percentage)
else:
    print("You failed, try again next year:", total_percentage)