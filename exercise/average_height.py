student_heights = [180, 124, 165, 173, 189, 169, 146]

sum = 0
len = 0

#You should not use the sum() or len() functions in your answer. 
#You should try to replicate their functionality using what you have learnt about for loops.
for heights in student_heights:
    len += 1
    sum += heights

print(len)
print(sum/len)