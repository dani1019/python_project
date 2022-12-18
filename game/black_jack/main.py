import cards as cd
import operation as op

#select the first card of user and computer
user_first_cards,computer_first_card= op.select_first_card()

print(f"your cards: {user_first_cards}")
print(f"Computer's first card: {computer_first_card}")


#Type 'y' to get another card type 'n' to pass:
op.add_card(user_first_cards,computer_first_card)

#if typing 'n'
#ex) your final hand : [9,10]
#Computer's final hand: [8,10]
#You win

