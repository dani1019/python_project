from random import randint

#print starting the game of uuess_number
def first_display():
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    #type easy or hard
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    EASY_CHANCE = 10
    HARD_CHANCE = 5

    #if typing easy is print(You have 10 attempts remaining to guess the number)
    if difficulty == "easy":
        print(f"You have {EASY_CHANCE} attempts remaining to guess the number")
    #if typing hard is print(You have 5 attempts remaining to guess the number)
    else:
        print(f"You have {HARD_CHANCE} attempts remaining to guess the number")
    
    #if no chance of attempts (0),You lose
    #if guess a number right You Win

def random_select_number():
    #select number through random proccess
    selected_number = randint(1,100)
    print(f"selected_number: {selected_number}")

#2) Make a guess number
def guess_number():
    #entered number must between 1 and 100
    guess_number = int(input("Make a guess number: "))
    #3) print Too high or Too low

    #4) print Guess again

    #5) repeat type easy or hard