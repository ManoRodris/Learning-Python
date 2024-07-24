import random

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

letters_list = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols_list = ['@','#','$','%','&','*']
numbers_list = ['0','1','2','3','4','5','6','7','8','9']

password_list = []
    
for n in range(letters):
    password_list.append(random.choice(letters_list))

for i in range(symbols):
    password_list.append(random.choice(symbols_list))

for m in range(numbers):
    password_list.append(random.choice(numbers_list))

random.shuffle(password_list)
password = ''.join(password_list)

print("Here is your password: " + password)


