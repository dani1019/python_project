import random
import my_module

random_integer = random.randint(1,10)

print(random_integer)

print(my_module.pi)

random_float = random.random()*5
#0*5 1*5  0 ~ 4.9999
print(random_float)

love_score = random.randint(1,100)
print(f"Your love_score is {love_score}")