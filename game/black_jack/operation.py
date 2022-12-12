import cards as cd
import random

#operate selecting card
def select_card(list_of_card, number_of_card):
    first_cards = random.sample(list_of_card, number_of_card)

    return first_cards

#select first card
def select_first_card():
    #select the first cards of user
    user_first_cards = select_card(cd.user_cards, 2)
    print(f"user_first_cards: {user_first_cards}")
    
    #select the first card of computer
    computer_first_card = select_card(cd.computer_cards, 1)
    print(f"computer_first_card: {computer_first_card}")

    return user_first_cards,computer_first_card


#if user type 'y', should select the card except to selected first cards
#select the card not to duplicate 
def add_card(user_first_cards,computer_first_card):
    whether_add_card = input("Type 'y' to get another card type 'n' to pass: ")
    if whether_add_card == 'y':
        select_card(cd.user_cards, 1)
    else:
        #print final result
        print_result(user_first_cards,computer_first_card)

#print final result
def print_result():
    print("Your final hand: {user_first_cards}")
    print("Computer's final hand: {computer_first_card}")



