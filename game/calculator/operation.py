def number_check(number):
    if type(number) != int:
        print("enter the number")


def operation(first_number, second_number, operation):
    
    if operation == "+":
        result_number = first_number + second_number
    elif operation == "-":
        result_number = first_number - second_number
    elif operation == "*":
        result_number = first_number * second_number
    else:
        result_number = first_number / second_number        

    print(f"{first_number} {operation} {second_number} = {result_number}")