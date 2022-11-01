import letter
import random

print("Welcome to the PyPassword Generator!")

#enter the number of letters
nr_letters= int(input("How many letters would you like in your password?\n"))

#select the letter that user enters the number 
letter_list = random.choices(letter.letters, k = nr_letters)

#enter the number of sumbols
nr_symbols = int(input(f"How many symbols would you like?\n"))

#select the symbols that user enters the number
symbol_list = random.choices(letter.symbols, k = nr_symbols)

#enter the number of numbers
nr_numbers = int(input(f"How many numbers would you like?\n"))

#select the numbers that user enters the number
number_list = random.choices(letter.numbers, k = nr_numbers)

print("Here is your password: ")

#combine three list
result_list = letter_list + symbol_list + number_list

print(result_list)

#result_list rearrange index randomly
random.shuffle(result_list)

print(shuffled_list)

#convert result_list to string
converted_string = ''.join(result_list)
print(converted_string)
