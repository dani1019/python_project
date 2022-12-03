#check if first_number is integer
def number_check(number):
    #if entered string is not number mark "enter the number"
    if not number.isnumeric():
        print("enter the number")
        return False
    return True

#print enter first number and user enter the first number
def enter_first_number():
    while True:
        first_number = input("What's the first number? ")
        #check if first_number is numberous
        #if first_number is numberous convert integer and return first_number
        #if first_number is string repeat question "What's the first number? "
        if number_check(first_number):
            first_number = int(first_number)
            return first_number
            break

#question user to enter operation
def enter_operation():
    operation = input("+\n-\n*\n/\nPick on operation: ")
    return operation

#print enter second number and user enter the second number
def enter_second_number():
    while True:
        second_number = input("What's the second number? ")
        #check if first_number is numberous
        #if second_number is numberous convert integer and return second_number
        #if second_number is string repeat question "What's the second number? "
        if number_check(second_number):
            second_number = int(second_number)
            return second_number
            break


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