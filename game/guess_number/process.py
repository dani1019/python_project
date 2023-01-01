from random import randint
EASY_CHANCE = 10
HARD_CHANCE = 5

#print starting the game of uuess_number
def first_display():
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    #type easy or hard
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    #if typing easy is print(You have 10 attempts remaining to guess the number)
    if difficulty == "easy":
        remained_chance = print_chance(EASY_CHANCE)
    #if typing hard is print(You have 5 attempts remaining to guess the number)
    else:
        remained_chance = print_chance(HARD_CHANCE)
    
    return remained_chance
    
    #if no chance of attempts (0),You lose
    #if guess a number right You Win

def print_chance(remained_chance):
    print(f"You have {remained_chance} attempts remaining to guess the number")

    return remained_chance

def random_select_number():
    #select number through random proccess
    selected_number = randint(1,100)
    print(f"selected_number: {selected_number}")

    return selected_number

#2) Make a guess number
def guess_number(selected_number,remained_chance):
    repeat_flag = True
    while repeat_flag:
        #entered number must between 1 and 100
        guess_number = int(input("Make a guess number: "))
        #3) print Too high or Too low
        if selected_number < guess_number:
            print("Too high")
        elif selected_number > guess_number:
            print("Too low")
        #substract 1 from remained chance

        #print remained chance
        else:
            print(f"you are correct. the number is {selected_number}")
            repeat_flag = False
            break
        remained_chance -= 1
        if remained_chance == 0:
            print("Game Over")
        else:
            print_chance(remained_chance)