# The good old if/elif/else:
# I have a number representing days of the week
# (1-7) (Sun - Sat) respectively

# Write me a function called get_day_name_if_else(num)
# It will take a num and return the day name (ug. 1 will return sunday)
# use if/elif/else:

# If elif option (NOT MATCH CASE)
def get_day_name_if_else(num):
    if num == 1:
        print("Sunday")
    elif num == 2:
        print("Monday")
    elif num == 3:
        print("Tuesday")
    elif num == 4:
        print("Wensday")
    elif num == 5:
        print("Thursday")
    elif num == 6:
        print("Friday")
    elif num == 7:
        print("Saturday")
    else:
        print("Invalid number.")

# A match case statement is an alternative to using multiple if, elif, and else statements
# It works by comparing a value (the "match") against several/multiple possible patterns (the "cases")
# When a match is found, the under that case runs
def get_day_name_match(num):
    match num:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print("Not a valid day")

get_day_name_match(1)
get_day_name_match(9)
get_day_name_match("test")

def is_weekend(daystr:str) -> bool:
    match daystr:
        case "Sunday":
            return True
        case "Saturday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case _:
            return False

# We can have multiple cases run the same code:
def is_weekend_shorter_match(daystr:str) -> bool:
    match daystr:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            raise ValueError(f"{daystr} is not a day stupid!")
        
print(is_weekend("Sunday"))
print(is_weekend("Monday"))
print(is_weekend_shorter_match("Sunday"))
print(is_weekend_shorter_match("Tuesday"))
print(is_weekend_shorter_match(":)"))