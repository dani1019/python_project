price = 0
#calculate the price of riding rollercoaster
print("Welcome to the rollercoaster!")

#Riding rollercoaster is permitted Taller than 120cm
height = int(input("What is your height in cm? "))

#if age is younger than 12 user should pay the bill $5
#if age is 12-18 user should pay the bill $7
#if age is older than 18 user should pay the bill $12
# free admission is offered to those who is aged 45- 55

if height > 120:
    age = int(input("How old are you? "))
    if age < 12:
        price = 5
    elif age <= 18:
        price = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        price = 12
    print(f"You should pay ${price}")
else:
    print("Sorry,you have to grow taller before you can ride.")


