#enter user's height
#enter user's weight
user_height = input("enter your height: ")
user_weight = input("enter your weight: ")


bmi = int(user_weight) / float(user_height) ** 2

print(bmi)

bmi_as_int = int(bmi)

print(bmi_as_int)