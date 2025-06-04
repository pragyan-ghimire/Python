# Logic: user enters the food and its prices, then we do total and display

#using set as it is ordered
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food (q to quit): ")
    if food == 'q':
        break
    price = float(input(f"Enter the price of {food}: "))
    foods.append(food)
    prices.append(price)

for price in prices:
    total += price

print(f"Total price: ${total}")
