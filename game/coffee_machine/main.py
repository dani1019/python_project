
seleced_drink = input("What would you like? (espresso/latte/cappuccino): ")
#1. if selecting the things you like to drink
#enter the inserted coin.
print("Please insert coin.")
number_10_yen = int(input("How many 10yen?: "))
number_100_yen  = int(input("How many 100yen?: "))

#make the key, value[] of kind of drink
#select the items that entered by user
#operate remained coin in coffee machine with inserted coin.
#print in change about money paid.
print(f"Here is 10yen change")
print(f"Here is your {seleced_drink} enjoy!")


#if you enter 'report' print the remain resources(water,milk,coffee,Money)
#the total resources water : 300ml, milk: 200ml, coffee 100g Money 0
#the quantity of making things.
#espresso: 50ml water,18g coffee, 150yen
#latte : 200ml water,24g coffee,150ml milk, 140yen
#cappuccino: 250ml water,22g coffee,100ml milk, 130yen