#This is how you work out whether if a particular year is a leap year.
#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100
#**unless** the year is also evenly divisible by 400

import process as pr

year = int(input("Which year do you want to check? "))
month = int(input("Which month do yo want to check? "))

#if value of return is false, leap year
if not pr.is_leap(year):
    print("leap year")
    pr.days_in_month(year,month,pr.is_leap(year))
else:
    print("not leap year")
    pr.days_in_month(year,month,pr.is_leap(year))
