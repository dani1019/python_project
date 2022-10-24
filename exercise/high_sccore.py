#enter subject's score
scores = input("Input a list of student scores ")

#convert string to list
list_of_scores = scores.split()

#convert string of list to integer
list_of_scores = [int(i) for i in list_of_scores]

big = 0
small = 0

#the biggest number move the end of list.
for i in range(len(list_of_scores)):
    if list_of_scores[i] > list_of_scores[i+1]:
        vig = list_of_scores[i]
        small = list_of_scores[i+1]
        list_of_scores[i+1] = big
        list_of_scores[i] = small

    print(type(result))
#[56, 63, 43]
#result[0] > result[1]
#big = result[0]
#small = result[1]
#result[1]= big
#result[0]= small
