import list_of_items as lst
#select the drink and insert coin
#return  selected_drink,number_10_yen,number_100_yen
def order_start():
    #select the drinking
    selected_menu = input("What would you like? (espresso/latte/cappuccino): ")
    if selected_menu == "report":
        #print remained quantity of coffee machine
        #쓴 물량에 대해 적용이 안됨 2023/01/24
        print_report()
        return
    else:
        #move select screen
        select_menu(selected_menu)

#select menu and calculate quantity of coffee machince to used quantity
def select_menu(selected_menu):
    #print insert to coin
    print("Please insert coin.")
    number_10_yen = int(input("How many 10yen?: "))
    number_100_yen  = int(input("How many 100yen?: "))

    if selected_menu == "espresso":
        #커피머신으로 부터 사용량 빼서 계산하는 처리
        calcute_quantity("espresso",number_10_yen,number_100_yen)
        #아래 글 프린트해주는 메소드 필요
        #Here is $2.42 in change.
        #Here is your latte enjoy.
    #if user select latte, execute calculating
    elif selected_menu == "latte":
        calcute_quantity("latte",number_10_yen,number_100_yen)
    #if user select cappuccino, execute calculating
    else:
        calcute_quantity("cappuccino",number_10_yen,number_100_yen)

#caculate sum of coffee machine's quantity to used quantity 
def calcute_quantity(kind_of_juice,number_10_yen,number_100_yen):
    for element in list(lst.coffee_machine):
        if element == "coin":
            inserted_coin = 10*number_10_yen + 100*number_100_yen
            #add inserted  coin to sum of coffee machine's coin
            lst.coffee_machine[element] += inserted_coin
            print(f"{element}: ￥{lst.coffee_machine[element]}")
            break;
        else:
            #sum of coffee machine's quantity - used quantity
            lst.coffee_machine[element] -= lst.kind_of_drink[kind_of_juice][element]

        print(f"{element}: {lst.coffee_machine[element]}ml")

#print remained quantity of coffee machine
def print_report():
    for material ,quantity in lst.coffee_machine.items():
        print(f"{material}: {quantity}ml")

    




            




