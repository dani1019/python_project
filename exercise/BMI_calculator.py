#User enter user's height,weight
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#calculate bmi
bmi = weight / height**2
print(type(bmi))
bmi_round = round(weight / height**2)
print(type(bmi_round))

#Tell user the interpretation of their BMI based on BMI value
if bmi < 18.5:
    print(f"Your BMI is {bmi_round}, you are under weight.")
elif bmi < 25:
    print(f"Your BMI is {bmi_round}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi_round}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi_round}, you are obese.")
else:
    print(f"Your BMI is {bmi_round}, you are clinically obese.")