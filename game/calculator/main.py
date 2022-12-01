import operation as op

#question user to enter first number
first_number = int(input("What's the first number? "))
#check entered number if it is number
op.number_check(first_number)
#question user to enter operation
operation = input("+\n-\n*\n/\nPick on operation: ")
#question user to enter second number
second_number = int(input("What's the next number? "))

op.operation(first_number, second_number, operation)

