#Your program should print each number from 1 to 100 in turn.
number = int(input("enter number "))

#When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("and so on")