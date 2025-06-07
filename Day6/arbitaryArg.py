# *args = allows you to pass multiple non-key arguments (stores in tuple)
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator


# *args
# def add(*nums): 
#     # print(type(nums))
#     # print(nums)
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1, 2, 3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end= " ")

# display_name("Prithvi", "Narayan", "Shah")

# **kwars
# def address(**locations):
#     print(locations)
#     # for location in locations:
#     #     print(locations.get(location))
#     # for value in locations.values():
#     #     print(value)
#     # print(locations.items())
#     for key, value in locations.items():
#         print(f"{key}: {value}")

# address(place = "Biratnagar", district = "Morang", country = "Nepal")

# *args and **kwargs (kwargs follows args)

def shipping_label(*args, **kwargs):
    print("This is a call for.")
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(f"{kwargs.get("realm")}, {kwargs.get("city")}")

shipping_label("Steward", "Zhuo", "Yifan",
               realm = "Middle",
               city = "Tian Mountain",
               sect = "Demon Scheming Sect"
               )