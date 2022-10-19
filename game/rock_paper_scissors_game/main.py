import picture
import random
import sys

#mark quesiton for user to enter the number
select_num =  input("What do  you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

#print try again when user entering character is empty or over 2 or string  
if select_num == '' or int(select_num) > 2 or select_num.isdigit() == False:
    print("try again。")
    sys.exit()

#change character entered by user string to integer
select_num_int = int(select_num)

#enter the picuture of rock,papper,scissors into the list
list_thing = []
list_thing.append(picture.rock)
list_thing.append(picture.paper)
list_thing.append(picture.scissors)

#print thing selected by user
print(list_thing[select_num_int])

#process random selection for computer's
random_select = random.choice(list_thing)
print(f"Computer choce\n {random_select}")
random_select_index = list_thing.index(random_select)

#judge whether if user win
#rock 0 rock 0   tie
#rock 0 paper 1  lose
#rock 0 scissors 2 win

#paper 1 rock 0 win
#paper 1 paper 1 tie
#paper 1 scissors 2 lose

#scissors 2 rock 0 lose
#scissors 2 paper 1 win
#scissors 2 scissors 2 tie

#rock 0 paper 1  lose
#paper 1 scissors 2 lose
#scissors 2 rock 0 lose

#rock 0 scissors 2 win
#paper 1 rock 0 win
#scissors 2 paper 1 win

if(select_num_int == 0) and (random_select_index == 2):
    print("You lose")
elif(select_num_int == 2) and (random_select_index == 0):
    print("You lose")
elif select_num_int > random_select_index:
    print("You win") 
elif select_num_int < random_select_index:
    print("You lose")