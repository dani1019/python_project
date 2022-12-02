import operation as op

end_check = True
#question user to enter first number
while end_check == True:
    #print enter first number and user enter the first number
    op.enter_first_number()
    #question user to enter operation
    op.enter_operation()
    #question user to enter second number
    op.enter_second_number()

    op.calculate(first_number, second_number, operation)

