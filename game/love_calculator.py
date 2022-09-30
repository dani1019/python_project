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
# my_name.count('t')
# my_name.count('r')
# my_name.count('u')
# my_name.count('e')

# their_name.count('t')
# their_name.count('r')
# their_name.count('u')
# their_name.count('e')

#count the times of letter that [L,O,V,E] from Two people's name


