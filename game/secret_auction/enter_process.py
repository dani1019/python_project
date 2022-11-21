
def enter_inform():
    user_name= input("What's your name?: ")
    #question user's bid
    user_bid = int(input("What's your bid: "))
    #save user's name and bid
    global user_info
    user_info[user_name] = user_bid

    print(user_info)