sum = 0
total2 = 0
for i in range(2,101, 2):
    sum += i

print(sum)

for number in range(1, 101):
    if number % 2 == 0:
        total2 += number

print(total2)