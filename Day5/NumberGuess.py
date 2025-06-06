# features that can be added: check whether guess is digit or not.  
                                # check for invalid range
import random

low = 0
high = 100
randomNumber = random.randint(low, high)
lives = 5

# print(randomNumber)

while lives>0:
    userGuess = int(input("Enter your guess (0 to 100): "))
    if userGuess == randomNumber:
        print(f"Your guess ({userGuess}) is correct.")
        break
    elif userGuess < randomNumber:
        lives -= 1
        print(f"Guess Higher. You have {lives} lives left.")
    else:
        lives -= 1
        print(f"Guess lower. You have {lives} lives left.")

if lives > 0:
    print("Congratulations. You won")
else:
    print("Better luck next time!")