## We are going to write a program that generates a random number and asks the user to guess it.
'''
If the player's guess is higher than the actual number, program displays "Lower number please", similarly if the user's guess is too low, the program prints "Higher number please". When the user guesses the correct number, program displays the number of guesses the player used to arrive at the number.
'''

import random

n = random.randint(1, 20)
p = -1
guesses = 1

while(p != n):
    p = int(input("Enter your number: "))
    if (p > n):
        print("Lower number please..")
        guesses += 1
    elif(p < n):
        print("Higher number please..")
        guesses += 1
        
print(f"You have guessed the number {n} correctly in {guesses} attempts")
        