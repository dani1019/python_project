
def enter_inform():
    user_name= input("What's your name?: ")
    #question user's bid
    user_bid = int(input("What's your bid: "))
    #make dictionary saving user's inform
    user_inform= {}
    #save user's name and bid
    user_inform[user_name] = user_bid

    print(user_inform)