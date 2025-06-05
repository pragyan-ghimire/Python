fruits = ["apple","orange","banana","coconut"]
vegetables = ("celery","carrots","potatoes")
meats = {"chicken","fish","turkey"}

groceries = [fruits, vegetables, meats] # 2d collection
print(groceries[0][0])

# for collection in groceries:
#     print(collection)

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

#Exercise
# tupple is a better choice as it is faster and unchangeable
symbols = [["1","2","3"], ["4","5","6"],["7","8","9"],["*","0","#"]]

for collection in symbols:
    for symbol in collection:
        print(symbol,end=" ")
    print()