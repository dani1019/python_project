#enter subject's score
scores = input("Input a list of student scores ")

#convert string to list
list_of_scores = scores.split()

#convert string of list to integer
list_of_scores = [int(i) for i in list_of_scores]

big = 0
small = 0

list_of_length = len(list_of_scores)

#the biggest number move the end of list.
#0-4 if loop of 3
# 3 > 4,  big = [3]  small = [4] [4] = big [3] = small
for i in range(list_of_length):
    # if i == list of length - 1, out of loop
    if i == list_of_length - 1:
        break;
    if list_of_scores[i] > list_of_scores[i + 1]:
        big = list_of_scores[i]
        small = list_of_scores[i+1]
        list_of_scores[i + 1] = big
        list_of_scores[i] = small


print(f"The highest score in the class is:{list_of_scores[list_of_length - 1]}")

#[56, 63, 43]
#result[0] > result[1]
#big = result[0]
#small = result[1]
#result[1]= big
#result[0]= small
