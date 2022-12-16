import cards as cd
import random

having_users_cards = []
having_computers_cards = []

#operate selecting card
def select_card(list_of_card, number_of_card):
    first_cards = random.sample(list_of_card, number_of_card)

    return first_cards

#select first card
def select_first_card():
    #select the first cards of user
    user_first_card = select_card(cd.user_cards, 2)
    #user_first_card add having_users_cards
    global having_users_cards
    having_users_cards += user_first_card
    
    #select the first card of computer
    computer_first_card = select_card(cd.computer_cards, 1)
    #computer_first_card add having_computers_cards
    global having_computers_cards
    having_computers_cards += computer_first_card

    return having_users_cards,having_computers_cards

#if user type 'y', should select the card except to selected first cards
#select the card not to duplicate 
def add_card(having_users_cards,having_computers_cards):
    whether_add_card = input("Type 'y' to get another card type 'n' to pass: ")
    if whether_add_card == 'y':
        #select one card and add having_users_cards
        having_users_cards += select_card(cd.user_cards, 1)
        print(f"users's cards : {having_users_cards}")
    else:
        #if sum of selected card is lower than 17, it should select one card.
        judge_lower_17(having_users_cards,having_computers_cards)
        

#if sum of selected card is lower than 17, it should select one card.
def judge_lower_17(having_users_cards,having_computers_cards):
    #check if sum of user having cards is lower than 17.
    if sum(having_users_cards) < 17:
        having_users_cards += select_card(cd.user_cards, 1)
        print_final_result(having_users_cards,having_computers_cards)
    else:
        print_final_result(having_users_cards,having_computers_cards)
    
    #check if sum of computer having cards is lower than 17.
    if sum(having_computers_cards) < 17:
        having_computers_cards +=  select_card(cd.computer_cards, 1)
        print_final_result(having_users_cards,having_computers_cards)
    else:
        print_final_result(having_users_cards,having_computers_cards)

#print final result
def print_final_result(having_users_cards,having_computers_cards):
    print(f"Your final hand: {having_users_cards}")
    print(f"Computer's final hand: {having_computers_cards}")

    if sum(having_users_cards) > sum(having_computers_cards):
        print("You win.")
    elif sum(having_users_cards) == sum(having_computers_cards):
        print("draw.")
    else:
        print("You lose.")


