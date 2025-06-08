# Iterables = an object/collection that can return its elements one at a time,
# allowing it to be iterable over in a loop

# List, tuple, set, dictionary, strings are iterables

numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number)

numbers = (1, 2, 3, 4, 5)
for number in reversed(numbers):
    print(number)

numbers = {1, 2, 3, 4, 5}
for number in numbers: # set cannot be reversed
    print(number)

name = "pragyan"
for character in name:
    print(character, end="")

capitals = {
    "Nepal": "Kathmandu",
    "India": "Delhi"
}
for key in capitals:
    print(key)
for val in capitals.values():
    print(val)