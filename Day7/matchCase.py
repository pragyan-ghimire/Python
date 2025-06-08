# match case is like switch of java

def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thrusday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"
       
day = day_of_week(1)
print(day)

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" |"Wednesday" |"Thrusday":
            return False
        case _:
            return False
       
print(is_weekend("Monday"))
