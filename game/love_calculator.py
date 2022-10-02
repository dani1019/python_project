#Take Two people's names and 
# check for the number of times the letter in word TRUE or Love occurs.

#enter name
my_name = input("What is your name? ")
their_name = input("What is their name? ")

lower_my_name = my_name.lower()
lower_their_name = their_name.lower()

word_true= "true"
word_love = "love"

true_count = 0
love_count = 0

#This times of Letter that Two people's name count
#count the times of letter that [T,R,U,E] from Two people's name
for i in word_true:
    true_count += lower_my_name.count(i)
    true_count += lower_their_name.count(i)

print(true_count)

#count the times of letter that [L,O,V,E] from Two people's name
for i in word_love:
    love_count += lower_my_name.count(i)
    love_count += lower_their_name.count(i)

print(love_count)

#ture_count,love_count convert string
#str(ture_count + love_count) = score
score_string= str(true_count) + str(love_count)
score_int = int(score_string)

#depending on condition, print result
if score_int < 10 or score_int > 90:
    print(f"Your score is {score_string}, you go together like coke and mentos.")
elif score_int >= 40 and score_int <= 50:
    print(f"Your score is {score_string}, you are alright together.")
else:
    print(f"Your score is {score_string}.")

