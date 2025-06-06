#shows menu of a restaurant

menu = {
    "Nan roti": "45",
    "Chicken curry": "270",
    "Burger":"200",
    "Pizza":"350",
    "Lemonade":"180"
}
order = []
total = 0
print("Welcome to Khaja Ghar")

viewMenu = menu.items()
items = menu.keys()

for item, price in viewMenu:
    print(f"{item:20}: Rs.{price}")

# while True:
#     userChoice = input("Enter order from menu(q to quit): ").capitalize()
#     if userChoice == "Q":
#         break
#     elif userChoice in items:
#         order.append(userChoice)
#         cost = menu.get(userChoice)
#         total = total + int(cost)
#     else:
#         print("Your ordered item is not in menu.")
#         break

# more efficient
while True:
    userChoice = input("Enter order from menu(q to quit): ").capitalize()
    if userChoice == "Q":
        break
    elif menu.get(userChoice) is not None:
        order.append(userChoice)
        total = total + int(menu.get(userChoice)) # we can also make value integer
    else:
        print("Your ordered item is not in menu.")
        break

    
print("Your order list:")
print(order)
print(f"Total: Rs.{total}")