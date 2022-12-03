#Calculator

first_number = input("What's the first number? ")
operation = input("+\n-\n*\n/\nPick on operation: ")


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

second_number = input("What's the second number? ")