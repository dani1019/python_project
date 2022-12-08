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
    #bug 전 연산에서 나온 결과에 다시 연산을 해야하는데,
    #첫 번쨰 입력한 숫자에 연산을 하게 된다.
    print(f"first_number_1: {first_number}")
    result_number = op.calculate(first_number, second_number, operation)

    #the result of calculation insert first_number
    first_number = result_number

    print(f"result_number: {result_number}")
    print(f"first_number_2: {first_number}")

    #check if continue to calculate
    #if stop to caculate return false
    # if continue to calculate return true
    result_flag = op.whether_continue_calculate(result_number)

    continue_flag = result_flag
