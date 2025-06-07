# position does not matter
#  Keyword argument follows positional argument

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(greeting="Good morning.", first="Nanda", title="Mr.", last="Bhattarai")
hello("Good morning.", first="Nanda", title="Mr.", last="Bhattarai")

print("1","2","3", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123 , first=456, last= 7890)
print(phone_num)