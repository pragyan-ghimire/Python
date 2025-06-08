# list comprehension = A concise way to create lists in Python
# compact and easier to read than traditional loops
# Syntax: [expression for value in iterable if condition]

# traditional loop
doubles = []
for x in range(1,11):
    doubles.append(x * 2)

print(doubles)

# list comprehension
doubles = [x*2 for x in range(1,11)]
print(doubles)

#----------------------
fruits = ["apple", "orange", "apple", "banana"]
upper_fruits = [fruit.upper() for fruit in fruits]
fruits_char = [fruit[0] for fruit in upper_fruits]
print(fruits_char)

#----------------------
numbers = [2, 6, 4, 9, 7]
odd = [num for num in numbers if num %2 != 0]
print(odd)