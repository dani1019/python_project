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

#Is the guessed letter in the word?
#if entered letter is correct, replace the blank with the letter
#elif entered letter is incorrect, lose a life
#print(f"You guessed {enter_letter}, that's not in the word. You lose a life.")
sum = 0

flag = True
remained_chance = 7
while flag == True:
    enter_letter = input("Guess a letter: ")
    brank_letter = len(answer_word)

#check if answer_word contains entered letter
    if enter_letter in answer_word:
        for index,answer_char in enumerate(list(answer_word)):
            print(f"index: {index}")
            #if enter_letter is included answer_char,
            # print the index,letter of answer_word, save print_word[index] = letter
            if enter_letter == answer_char:
                print_word[index] = answer_char
            #bug 맨 나중에 중간의 알파벳을 입력하면, Congratulation! Mission Complete!"가 복수로 출력된다.
            if print_word.count("-") == 0:
                print("Congratulation! Mission Complete!")
                flag = False
                print("1")
                break
    #minus wrong_count and print hang's picture
    else:
        remained_chance -= 1
        print(remained_chance)
        print(art.stages[remained_chance])
        if remained_chance == 0:
            print("Game Over")
            flag = False
    print(' '.join(print_word))


#Are all the blacks filed
#If all the blacks filed Game over
#Elif all the blacks don't filled move the screen guessing a letter

#Have they run out of lives
#If Yes Game over
#elif move the screen guessing a letter