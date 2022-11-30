leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
not_leap_year =  [31,28,31,30,31,30,31,31,30,31,30,31]

#judge if year is leap year 
def is_leap(year):
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

#print the days of month
def days_in_month(year,month,bool):
    if not bool:
        print(leap_year[month -1])
    else:
        print(not_leap_year[month - 1])
    