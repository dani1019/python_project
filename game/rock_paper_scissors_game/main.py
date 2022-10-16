import picture
import random

#mark quesiton for user to enter the number
select_num =  int(input("What do  you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

#enter the picuture of rock,papper,scissors into the list
list_thing = []
list_thing.append(picture.rock)
list_thing.append(picture.paper)
list_thing.append(picture.scissors)

#print thing selected by user
print(f"{select_num}\n{list_thing[select_num]}")

#process random selection for computer's
random_select = random.choice(list_thing)
print(random_select)
print(list_thing[random_select])
# print(f"Compuer  chose:\n {random_select}")

#judge whether if user win
#rock 0 < paper 1
#rock 0 > scissors 2
#paper 1 < scissors 2
# if select_num > random_select_index:
#     if(select_num == 0) and (random_select_index == 2):
#         print("You lose.")
#     else:
#         print("You win.")
# else:
#     print("You lose.")
        
#rock 0, paper 1, scissors 2

#print thing user selecting, computer's

#mark that which win is

