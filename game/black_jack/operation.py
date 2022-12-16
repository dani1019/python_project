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


#합계에서 하나의 카드를 더한 후에도 유저 컴퓨터 어느 중하나라도, 17이하면 다시실행해야 함.
#예 유저 17, 컴퓨터 10 → sum_user >= 17 and sum_com < 17
# 유저 17, 컴퓨터 15  → sum_user >= 17 and sum_com < 17 카드하나 추가 
#if sum of selected card is lower than 17, it should select one card.
def judge_lower_17(having_users_cards,having_computers_cards):
    flag_over_17 = True

    sum_user= sum(having_users_cards)
    sum_com= sum(having_computers_cards)   
    while flag_over_17:
        #the sum of user's cards < 17, the sum of computer's cards >=17
        #→select one more user's card
        if sum_user < 17 and sum_com >= 17:
            having_users_cards += select_card(cd.user_cards, 1)
            sum_user = sum(having_users_cards)

            #if sum of user's cards harder than 16, while escape flag_over_17
            if sum_user >= 17:
                break

        #the sum of user's cards >= 17, the sum of computer's cards < 17
        #→select one more computer's card     
        elif sum_user >= 17 and sum_com < 17:
            having_computers_cards +=  select_card(cd.computer_cards, 1)
            sum_com = sum(having_computers_cards)

            #if sum of computer's cards harder than 16, while escape flag_over_17
            if sum_com >= 17:
                break

        #the sum of user's cards < 17, the sum of computer's cards < 17
        #→select both of cards     
        elif sum_user < 17 and sum_com < 17:
            having_users_cards += select_card(cd.user_cards, 1)
            having_computers_cards +=  select_card(cd.computer_cards, 1)

            sum_user = sum(having_users_cards)     
            sum_com = sum(having_computers_cards)

        #the sum of user's cards > 17, the sum of computer's cards > 17
        #→not select card
        else:
            pass

# def judge_sum_over_17(having_users_cards,having_computers_cards):



#print the result
def print_result(having_users_cards,having_computers_cards):
    print(f"Your final hand: {having_users_cards}")
    print(f"Computer's final hand: {having_computers_cards}")

    if sum(having_users_cards) > sum(having_computers_cards):
        print("You win.")
    elif sum(having_users_cards) == sum(having_computers_cards):
        print("draw.")
    else:
        print("You lose.")


