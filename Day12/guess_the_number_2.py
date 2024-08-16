from art import logo
from random import randint

def difficulty_level(complexity):
    if complexity == "easy":
        return 10
    elif complexity == "hard":
        return 5
    
def decrease_of_attempts(attempts):
    return attempts - 1

def check_answer(attempts):
    if attempts != 0:
        print("Guess again")
    else:
        print("Game over")

def the_game():
    number_of_attempts = difficulty_level(difficulty)
    computer_number = randint(1, 100)
    print(computer_number)
    win = False
    
    while number_of_attempts != 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > computer_number:
            print("Too high")
            number_of_attempts = decrease_of_attempts(number_of_attempts)
        elif guess < computer_number:
            print("Too low")
            number_of_attempts = decrease_of_attempts(number_of_attempts)
        else:
            print(f"You got it! The answer was {computer_number}")
            break

        check_answer(number_of_attempts)


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficult. Type 'easy' or 'hard': ")

the_game()