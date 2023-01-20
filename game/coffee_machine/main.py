#select the drink and insert coin
import proccess as pr
selected_menu,number_10_yen,number_100_yen = pr.order_start()

pr.select_menu(selected_menu,number_10_yen,number_100_yen)


#if you enter 'report' print the remain resources(water,milk,coffee,Money)
#the total resources water : 300ml, milk: 200ml, coffee 100g Money 0
#the quantity of making things.
#espresso: 50ml water,18g coffee, 150yen
#latte : 200ml water,24g coffee,150ml milk, 140yen
#cappuccino: 250ml water,22g coffee,100ml milk, 130yen