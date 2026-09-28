## Using basic python program create a childhood game called "Snake-Water-Gun" having user input.

import random

'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1, 0, -1])
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youdict[youstr]


print(f"You chose: {reversedict[you]}\nComputer chose: {reversedict[computer]}")

if(computer == you):
    print("It's a DRAW..")

else:
    if(computer == -1 and you == 1): #(computer - you) == -2
        print("You WIN!!!")
    elif(computer == 0 and you == 1): #(computer - you) = -1
        print("You LOSE...")
    elif(computer == -1 and you == 0): #(computer - you) = -1
        print("You LOSE...")
    elif(computer == 0 and you == -1): #(computer - you) = 1
        print("You WIN!!!")
    elif(computer == 1 and you == 0): #(computer - you) = 1
        print("You WIN!!!")
    elif(computer == 1 and you == -1): #computer - you) = 2
        print("You LOSE...") 
    
        ## OR ##
    
    # elif((computer - you) == -1 or (computer - you) == 2):
    #     print("You LOSE!")
    
    # else:
    #     print("You WIN!!!")