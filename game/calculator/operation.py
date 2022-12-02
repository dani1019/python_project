#check if first_number is integer
def number_check(number):
    #if entered string is not number mark "enter the number"
    if not number.isnumeric():
        print("enter the number")
        isnumeric = False

#print enter first number and user enter the first number
def enter_first_number():
        first_number = input("What's the first number? ")
        #check if first_number is integer
        number_check(first_number)

#question user to enter operation
def enter_operation():
    operation = input("+\n-\n*\n/\nPick on operation: ")

#print enter second number and user enter the second number
def enter_second_number():
    second_number = input("What's the first number? ")
    #check if first_number is integer
    number_check(second_number)



def calculate(first_number, second_number, operation):
    
    if operation == "+":
        result_number = first_number + second_number
    elif operation == "-":
        result_number = first_number - second_number
    elif operation == "*":
        result_number = first_number * second_number
    else:
        result_number = first_number / second_number        

    print(f"{first_number} {operation} {second_number} = {result_number}")