#build an automatic pizza order program
#customize the codition by options below 
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

price = 0
#print first sentence
print("Welcome to Python Pizza Deliveries!")

#question user to setting option
size = input("What size pizza do you want? S, M, or L  ")
add_pep = input("Do you want pepeeroni?  Y or N ")

if size == "S":
    price += 15
    if add_pep == "Y":
        price += 2
        print(price)
elif size == "M":
    price += 20
    print(f"price1: {price}")
    print(price)
    if add_pep == "Y":
        price += 3
else:
    price += 15
    if add_pep == "Y":
        price += 3

if add_pep == "Y":
    price += 1
extra_pizza = input("Do you want extra cheese? Y or N ")

if extra_pizza == "Y":
    price += 1

print(f"Your final bill is: ${price}")
