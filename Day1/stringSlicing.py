# slicing = create a substring by extracting elements from another string 
# indexing[] or slice()
# [start:stop:step]

# # starting index 
name = "Pragyan Ghimire"
# first_name = name[0]

# # starting(inclusive) and stopping index(exclusive) 
# first_name = name[0:7] # or name[:7]
# last_name = name[8:] # or name[8:15]
# print(first_name + last_name)

# #stepping
# first_name = name[0:7:2] # name[:7:2]
# print(first_name)

# reversed_name = name[::-1]
# print(reversed_name)


#using slice function
website1 = "http://google.com" 
website2 = "http://booking.com" 
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])