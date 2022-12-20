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

def print_having_cards(users_card,computer_card):
    print(f"your cards: {users_card}")
    print(f"Computer's card: {computer_card}")

#if user type 'y', should select the card except to selected first cards
#select the card not to duplicate
def add_card(having_users_cards,having_computers_cards):
    whether_add_card = input("Type 'y' to get another card type 'n' to pass: ")
    #사용자가 카드를 더 뽑고 싶을 때 처리
    if whether_add_card == "y":
        #the sum of selected card is over 21,no more select the card.
        if sum(having_users_cards) > 21:
            print("because sum of your cards is over 21,you can't select card.")
        else:
            having_users_cards += select_card(cd.user_cards, 1)
            #if sum of selected card is lower than 17, it should select one card.
            judge_lower_17(having_users_cards,having_computers_cards)
    else:
        #if sum of selected card is lower than 17, it should select one card.
        judge_lower_17(having_users_cards,having_computers_cards)
    
    print_result(having_users_cards, having_computers_cards)


#if sum of selected card is lower than 17, it should select one card.
def judge_lower_17(having_users_cards,having_computers_cards):

    flag_lower_17 = True
    sum_user= sum(having_users_cards)
    sum_com= sum(having_computers_cards)

    user_card_list = having_users_cards
    computer_card_list = having_computers_cards
    
    while flag_lower_17:
        #the sum of user's cards < 17, the sum of computer's cards >=17
        #→select one more user's card
        if sum_user < 17 and sum_com >= 17:
            user_card_list += select_card(cd.user_cards, 1)
            sum_user = sum(user_card_list)

        #the sum of user's cards >= 17, the sum of computer's cards < 17
        #→select one more computer's card     
        elif sum_user >= 17 and sum_com < 17:
            computer_card_list +=  select_card(cd.computer_cards, 1)
            sum_com = sum(computer_card_list)

        #the sum of user's cards < 17, the sum of computer's cards < 17
        #→select both of cards     
        elif sum_user < 17 and sum_com < 17:
            user_card_list += select_card(cd.user_cards, 1)
            computer_card_list +=  select_card(cd.computer_cards, 1)

            sum_user = sum(user_card_list)  
            sum_com = sum(computer_card_list)
            
        #the sum of user's cards > 17, the sum of computer's cards > 17
        #→not select card
        else:
            flag_lower_17 = False
        
    #return user's cards and computer's card
    return user_card_list,computer_card_list

#print final result
def print_result(having_users_cards,having_computers_cards):
    print(f"Your final hand: {having_users_cards}")
    print(f"Computer's final hand: {having_computers_cards}")

    judge_win(having_users_cards,having_computers_cards)

#judge whether is win
def  judge_win(having_users_cards,having_computers_cards):
    #사용자 21 초과, 컴퓨터 21 미만 → 컴퓨터 승
    #사용자 21 미만, 컴퓨터 21 초과 → 사용자 승
    #사용자 21 초과, 컴퓨터 21 초과 → 다시 실행
    #사용자 21 미만, 컴퓨터 21미만 → 21에 가까운 수가 승리

    judge_num = 21
    sum_users = sum(having_users_cards)
    sum_coms = sum(having_computers_cards)

    #if sum_users is higher than 21, sum_coms is lower than 21
    #computer win
    if sum_users > 21 and sum_coms < 21:
        print("You lose.")

    #if sum_users is lower than 21, sum_coms us higher than 21
    #user win       
    elif sum_users < 21 and sum_coms > 21:
        print("You win.")

    #if both user and computer is higher than 21
    #start game again"    
    elif sum_users > 21 and sum_coms > 21:
        print("Please start game again")

    #if both user and computer is lower than 21
    #close to 21, which win
    else:
        if judge_num - sum_users < judge_num - sum_coms:
            print("You win.")
        elif judge_num - sum_users == judge_num - sum_coms:
            print("It's draw")
        else:
            print("You lose.")


