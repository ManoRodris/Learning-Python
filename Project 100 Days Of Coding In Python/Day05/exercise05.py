import random

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

letters_list = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols_list = ['@','#','$','%','&','*']
numbers_list = ['0','1','2','3','4','5','6','7','8','9']

letters_in_password = ""
symbols_in_password = ""
numbers_in_password = ""

for n in range(0, letters):
    char = random.choice(letters_list)
    letters_in_password += random.choice([char.upper(), char.lower()])

for i in range(0, symbols):
    symbols_in_password += random.choice(symbols_list)

for m in range(0, numbers):
    numbers_in_password += random.choice(numbers_list)

password = letters_in_password + symbols_in_password + numbers_in_password

print("Here is your password: " + password)