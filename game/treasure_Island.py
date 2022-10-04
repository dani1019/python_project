#print starting game
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
#left or right
#left → advance the next quesition
#right → print Game over
want_go = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ')
if want_go == "left":
    #swim or wait
    #swim  → print Game over
    #wait → advance the next quesition
    how_to_go = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if how_to_go ==  "wait":
        #Which door?
        #Red or Blue or Yellow
        #Red or Blue → Game Over
        # Yellow  → You Finish
        select_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        select_door_lower = select_door.lower()
        print(select_door_lower)
        if select_door_lower == "red" or select_door_lower == "blue":
            print("It's a room full of fire. Game Over.")        
        elif select_door_lower == yellow:
            print("You found the treasure! You Win!")
        else:
            print('Please enter "red" or "blue" or "yellow"')  
    elif how_to_go == "swim":
        print("game over.")
    else:
        print('Please enter "swim" or "wait"')
elif want_go == "right":
    print("game over.")
else:
    print('Please enter "left" or "right"')