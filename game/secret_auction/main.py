import enter_process as ep

print("Welcome to the secret auction program")
#question user's name

user_info = {}

ep.enter_inform()

continue_flag = True

#questsion there is other bidders?
while continue_flag == True:
    exist_other_bidders = input("Are there any other bidders? Type 'yes' or 'no.'")
    if exist_other_bidders == "yes":
        ep.enter_inform()
    else:
        print(f"The winner is James with a bid of $142.")
        continue_flag = False
        
