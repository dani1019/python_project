import operation as op

end_check = True
#print enter first number and user enter the first number
first_number = op.enter_first_number()
#question user to enter operation
operation = op.enter_operation()
#question user to enter second number
second_number = op.enter_second_number()

op.calculate(first_number, second_number, operation)

