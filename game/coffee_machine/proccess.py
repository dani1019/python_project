import list_of_items as lst
#select the drink and insert coin
#return  selected_drink,number_10_yen,number_100_yen
def order_start():
    #select the drinking
    selected_menu = input("What would you like? (espresso/latte/cappuccino): ")
    #enter the inserted coin.
    print("Please insert coin.")
    number_10_yen = int(input("How many 10yen?: "))
    number_100_yen  = int(input("How many 100yen?: "))

    return selected_menu,number_10_yen,number_100_yen

def select_menu(selected_menu,number_10_yen,number_100_yen):
    #caculate the remanied quantity of coffee machince - usered quantity
    if selected_menu == "report":
        pass
    else:
        #if user select espresso, execute calculating
        if selected_menu == "espresso":
            calcute_quantity("espresso")
        #if user select latte, execute calculating
        elif selected_menu == "latte":
            calcute_quantity("latte")
        #if user select cappuccino, execute calculating
        else:
            calcute_quantity("cappuccino")
            lst.coffee_machine["water"] - lst.kind_of_drink["espresso"]["water"]
            lst.coffee_machine["coffee"] - lst.kind_of_drink["espresso"]["coffee"]
            lst.coffee_machine["milk"] - lst.kind_of_drink["espresso"]["milk"]
            lst.coffee_machine["coin"] - lst.kind_of_drink["espresso"]["coin"]

            print(lst.coffee_machine["water"])
            print(lst.coffee_machine["coffee"])
            print(lst.coffee_machine["milk"])
            print(lst.coffee_machine["coin"])

def calcute_quantity():
    for index,matarial in enumerate(lst.coffee_machine):
        print(coffee_machine[index])




            




