#This is how you work out whether if a particular year is a leap year.
#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100
#**unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

def is_leap():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return False
            else:
                return True
        else:
            return False
    else:
        return True

#if value of return is false, leap year
if not is_leap():
    print("leap year")
else:
    print("not leap year")
