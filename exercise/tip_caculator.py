#enter total bill
total_bill = float(input("What was tha total bill? "))

#enter percentage of tip
percentage_tip = int(input("What percentage  tip would you like to give? 10, 12, or 15? "))
tip_price = total_bill / percentage_tip

#enter split number(nuber of person)
number_of_person = int(input("How many people to split the bill? "))

#caculate how much Each person should pay
result = (total_bill + tip_price) / number_of_person
result_round = round(result, 2)

#print result
print(f"Each person should pay: ${result_round}")
