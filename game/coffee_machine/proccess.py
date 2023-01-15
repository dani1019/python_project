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

def operate(selected_menu,number_10_yen,number_100_yen):
    #caculate the remanied quantity of coffee machince - usered quantity
    if selected_menu == "report":


