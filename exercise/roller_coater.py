print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("How old are you? "))
    price = 0
    if age <= 12:
        price += 12
    elif age < 18:
        price += 15
    else:
        price += 18
    wants_photo = input("Do you want a photo taken? Y or N. ")

    if wants_photo == "Y":
        price += 3
    print(f"You should pay ${price}")
else:
    print("Sorry,you have to grow taller before you can ride.")