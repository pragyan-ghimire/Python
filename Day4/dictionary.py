# dictionary = a collection of {key:value} pairs ordered
#             and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India":"New Delhi",
            "Nepal":"Kathmandu"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("USA"))
if capitals.get("China"):
    print(capitals.get("China"))
else:
    print("Capital of China doesn't exists.")

capitals.update({"Germany":"Berlin"}) # add a capital
capitals.update({"USA": "Uganda"}) # change a capital
capitals.pop("USA") # remove a capital
capitals.popitem() # removes latest key value pair
print(capitals)
# capitals.clear()

keys = capitals.keys() # returns all keys available
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

items = capitals.items()
print(items)

for key, value in items:
    print(f"{key}: {value}")