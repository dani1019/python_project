import picture
import random

#mark quesiton for user to enter the number
input("What do  you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")

#process random selection for computer's
list_thing = []
list_thing.append(picture.rock)
list_thing.append(picture.paper)
list_thing.append(picture.scissors)

random_select = random.choice(list_thing)
print(random_select)

#judge whether if user win
#rock 0, paper 1, scissors 2

#print thing user selecting, computer's

#mark that which win is

