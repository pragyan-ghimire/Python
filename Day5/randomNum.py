import random

# print(help(random))

print(random.randint(1,6)) # random integer number from 1 to 6

number = random.random() # floating point number between 0 and 1
print(f"{number:.2f}")

options = ("rock", "paper", "scissors")
option = random.choice(options) # generates random option from options
print(option)

cards = ["1","2","3","4"]
random.shuffle(cards)
print(cards)