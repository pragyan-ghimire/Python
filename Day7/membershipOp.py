# Membership operators = used to test whether a value or variable is found in a sequence
# (string, list, tuple, set, or dict)
# in, not in 

word = "fasinating"

letter = input("Guess a character(a-z): ").lower()

# if letter.isdigit():
#     print("Invalid input.")
# elif letter in word:
#     print("Your guess is correct.")
# else:
#     print("Incorrect guess.")

if letter.isdigit():
    print("Invalid input.")
elif letter not in word:
    print("Incorrect guess.")
else:
    print("Your guess is correct.")

# --------------
characters = {"Roman", "Alexander", "Luna", "Kevin"}

character = input("Enter a character from 'Descended from Divinity': ").capitalize()

if character in characters:
    print(f"{character} is available.")
else:
    print(f"{character} is not the part of the show.")


# -------------------
main_characters = {"Magic Emperor": "Zhuo Yifan",
                   "Descended from Divinity": "Roman Dmitri",
                   "Solo Leveling": "Sung Jinwoo",
                   "The Beginning After the End": "Arthur"
                   }

manhua = input("Enter name of the manhua: ")

if manhua in main_characters:
    print(f"{main_characters[manhua]} is the main character of {manhua}")
else:
    print(f"{manhua} was not found")