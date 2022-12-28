import process as ps

#print starting the game of uuess_number
remained_chance = ps.first_display()

#select the number user getting the correct answer
selected_number= ps.random_select_number()

#Make a guess number
ps.guess_number(selected_number,remained_chance)
