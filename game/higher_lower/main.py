import process as pr
#1.make a key,value name of list = {neymar, cobi,endo}
#{
# neymar: [a soccer player, Brazil, 50] ,
# cobi : [a basketball player, USA, 49]  
#}

#3.the random selecting compare A
#select value from key
#4.the random selecting AgainB
#select value from key
selected_list= pr.random_select()

#5.print compare A: neymar , a soccer player, from Brazil
#6.print Against B : Cobi, a basketball player, from USA
#7.print Who has more followers Type 'A' or 'B'
pr.print_subject(selected_list)

#8-1.if corrected answer will be print you are correct score +5 
#8-2if wronged answer will be print you are wrong score -5
#9.until score will be 0, contiune the game, if score is 0, and Game over