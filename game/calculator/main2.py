#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

num1= int(input("What's the first number? "))
num2= int(input("What's the second number? "))

#print(operation[enter_operation](num1, num2))

#for key, value in operation.items():
##    if  enter_operation == key:
#       print(value(num1, num2))

for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation from the line above.")

calculate_function = operation[operation_symbol]

answer = calculate_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")