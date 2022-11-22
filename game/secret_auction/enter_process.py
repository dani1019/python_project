import main

def enter_inform():
    user_name= input("What's your name?: ")
    #question user's bid
    user_bid = int(input("What's your bid: "))
    #save user's name and bid
    main.user_info[user_name] = user_bid
    
    print(main.user_info)