import random
import art
import word
#start
print(art.logo)

#Generate a random word
answer_word = random.choice(word.word_list)

print(answer_word)

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

wrong_count = 7

#check if answer_word contains entered letter
if enter_letter in answer_word:
    print("enter_letter")
    for index,answer_char in enumerate(list(answer_word)):
        #if enter_letter is included answer_char,
        # print the index,letter of answer_word, save print_word[index] = letter
        if enter_letter == answer_char:
            print_word[index] = answer_char

#minus wrong_count and print hang's picture
else:
    wrong_count -= 1
    print(art.stages[wrong_count])
print(''.join(print_word))


#Are all the blacks filed
#If all the blacks filed Game over
#Elif all the blacks don't filled move the screen guessing a letter

#Have they run out of lives
#If Yes Game over
#elif move the screen guessing a letter