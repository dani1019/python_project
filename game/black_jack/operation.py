import cards as cd
import random

#select randomed card
def select_first_card():
    #select the first cards of user
    user_first_cards = random.choices(cd.cards, k= 2)
    #select the first card of computer
    computer_first_card = random.choices(cd.cards)

    return user_first_cards,computer_first_card

#def select_one_card():

#if user type 'y', should select the card except to selected first cards
def add_card():
    whether_add_card = input("Type 'y' to get another card type 'n' to pass:")
    if whether_add_card == 'y':

