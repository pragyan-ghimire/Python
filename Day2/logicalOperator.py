temp = float(input("Enter the temperature: "))

if temp >=0 and temp <=30:
    print("The temperature is good today!")
    print("Lets go to travel a place near by")
elif temp < 0 or temp > 30:
    print("The temperature is bad today")
else:
    print("Don't know")