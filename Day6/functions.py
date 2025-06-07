
def happy_birthday(name):
    print(f"Happy birthday {name}")

happy_birthday("Pragyan")

# order of the passed argument and parameters matters
def contact(name, age, email):
    print(f"Hello, {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")

contact("Pragyan", 21, "something@gmail.com")

def add(a, b):
    return a+b

result = add(2,3)
print(f"Result: {result}")

