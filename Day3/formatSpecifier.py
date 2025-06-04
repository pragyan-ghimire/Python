# format specifiers = {value:flags} format a value based on what 
#                     flags are inserted

price1 = 3.14158
price2 = -3545.345
price3 = 235

# floating precision
print(f"Price 1 is ${price1:.4f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

# spacing
print(f"Price 1 is ${price1:10}") # has 10 spaces(columns to insert value)
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:010}") # empty space is filled by "0"
print(f"Price 3 is ${price3:<10}") # left justified(right justified by default)
print(f"Price 3 is ${price3:^10}") # center justified
print(f"Price 3 is ${price3:+}") # for positive signed
print(f"Price 2 is ${price2:,}") # thousand separator

#combination
print(f"Price 2 is ${price2:+,.2f}") # the specifier should be in correct place