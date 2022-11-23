user_info = {}

def enter_inform():
    print("aa")
    user_name= input("What's your name?: ")
    #question user's bid
    user_bid = int(input("What's your bid: "))
    user_info[user_name] = user_bid
    #save user's name and bid
    user_info[user_name] = user_bid
    
    print(user_info)
    #select the highest price
    print(f"max(user_info): {max(user_info)}")