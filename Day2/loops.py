import time
# while loop 
name = ""

while len(name) == 0:
    name = input("Enter your name: ")
print(name)

# for loop
for i in range(10):
    print(f"for loop: {i+1}")
for i in range(50,60): # first number is inclusive and second is exclusive
    print(i)
for i in range(50,60,2): # first number is inclusive and second is exclusive
    print(i)
for i in "Pragyan":
    if i == "a":
        print(i)

# timer 
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("have a good day")

# nested loops
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter the symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end = "") # end = "" will not let to move to next line
    print()