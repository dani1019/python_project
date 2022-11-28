#This is how you work out whether if a particular year is a leap year.
#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100
#**unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

#leap year
#evenly divisible by 4 
if year % 4 == 0:
    #*except** evenly divisible by 100
    if year % 100 != 0:
        #evenly divisible by 400
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("not leap year")
else:
    print("not leap year")
