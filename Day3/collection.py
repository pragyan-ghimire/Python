# collection = single "variable" used to store multiple values
# List = [] ordered and changeable; dublication ok
# Set = {} unordered and immutable, but add/remove ok. no duplication
# Tuple = () ordered and unchangeable. duplicates ok. faster

# we can used index operator on list

# list
fruits = ["apple", "orange", "guava","guava"]

print(fruits)
print(fruits[2])
print(fruits[0:2])

for fruit in fruits:
    print(fruit)


# methods available for collections

print(dir(fruits)) # prints all available methods
print(help(fruits)) # shows description of the methods
print(len(fruits))
print("orange" in fruits) # returns boolean

#changeable property
fruits[0] = "mango"
fruits.append("nascent breaker")
fruits.remove("guava")
fruits.insert(0,"reincarnation fruit")
fruits.sort() # alphabetical order
fruits.reverse() # reverse order(after sorting)
# fruits.clear()
print(fruits)
print(fruits.index("apple"))

print(fruits.count("guava"))

#set (indexing cannot be used)
fruits = {"apple", "orange", "guava"}
print(fruits)
print(dir(fruits)) # prints all available methods
print(help(fruits)) # shows description of the methods
print(len(fruits))
print("orange" in fruits) # returns boolean
fruits.add("pineapple")
fruits.remove("orange")
fruits.pop() # removes first element (but it will be random)
# fruits.clear()
print(fruits)

#tuples(dir, help, len)
fruits = ("apple","apple", "orange", "guava")
print(fruits.index("apple"))
print(fruits.count("apple"))
print(fruits)
for fruit in fruits:
    print(fruit)

# fruits[0] = "banana" # shows error