import enter_process as ep
from os import system

print("Welcome to the secret auction program")
#question user's name

user_info = {}
ep.enter_inform()
continue_flag = True

#questsion there is other bidders?
while continue_flag == True:
    exist_other_bidders = input("Are there any other bidders? Type 'yes' or 'no.' ")
    #if user answer yes, entered infrom is deleted, other user can answer the question
    if exist_other_bidders == "yes":
        #clear entered inform before
        system('cls')
        ep.enter_inform()

    elif exist_other_bidders == "no":
        max_name, max_price = ep.result_max()
        print(f"The winner is {max_name} with a bid of ${max_price}.")
        continue_flag = False
    else:
        print("please enter yes or no.")
        
