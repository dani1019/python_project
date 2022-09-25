#calculate how left your life

#enter user's age
age = input("What is your currenct age? ")

#print how many remains user's life in days and years and weeks
#assume that death is 90
left_life = 90 - int(age)
left_life_days = left_life * 365
left_life_weeks = left_life * 52

#print message
message = f"you have {left_life_days} days, {left_life_weeks} weeks, {left_life} years"
print(message)