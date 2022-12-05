import operation as op

#print enter first number and user enter the first number
first_number = op.enter_first_number()

continue_flag = True

#if calculating continue,
while continue_flag:
    second_number = op.enter_second_number()
    #question user to enter operation
    operation = op.enter_operation()
    #question user to enter second number
    result_number = op.calculate(first_number, second_number, operation)

    #버그-- no선택시, continue_flag == False가 되어야 하는데 안되고 있음
    op.whether_continue_calculate(result_number)