#string type
string1 = "You can"
string2 = "do it."
sentence = string1 + " " + string2
print(sentence)
print(type(sentence))

#integer type
age = 21
print(age)
print(type(age))
# print("I am " + age +"years old") results into TypeError: can only concatenate str (not "int") to str
print("I am " + str(age) +" years old") #type casting
print(f"I am {age} years old") #using f string

#float type
marks = 85.5
print(marks)
print(type(marks))
print(f"You obtained {marks} out of 100.")

#boolean type
passed = True
print(passed)
print(type(passed))
print(f"You have passed the exam : {passed}")