user_info = {}

#question user to name and price
def enter_inform():
    user_name= input("What's your name?: ")
    #question user's bid
    user_bid = int(input("What's your bid: "))
    user_info[user_name] = user_bid
    #save user's name and bid
    user_info[user_name] = user_bid

#print the highest price,people
def result_max():
    max_name = max(user_info, key=user_info.get)
    max_price = max(user_info.values())
    
    print(max_name,max_price)
    return max_name, max_price
