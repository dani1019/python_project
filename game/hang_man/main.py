import random
import art
import word
#start
print(art.logo)

#Generate a random word
answer_word = random.choice(word.word_list)

#make list that print word at first
print_word = []
#Generate as many blanks as letters in word
for i in range(len(answer_word)):
    print_word.append("-")
print(' '.join(print_word))

#Ask the user to guess a letter
enter_letter = input("Guess a letter: ")

#Is the guessed letter in the word?
#if entered letter is correct, replace the blank with the letter
#elif entered letter is incorrect, lose a life
#print(f"You guessed {enter_letter}, that's not in the word. You lose a life.")

#Are all the blacks filed
#If all the blacks filed Game over
#Elif all the blacks don't filled move the screen guessing a letter

#Have they run out of lives
#If Yes Game over
#elif move the screen guessing a letter