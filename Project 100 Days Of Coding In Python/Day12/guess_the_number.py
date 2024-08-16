from art import logo
import random

def guess_the_number(complexity):
    number_from_computer = random.randint(1, 100)

    win = False

    if complexity == "easy":
        num_of_attempts = 10
    elif complexity == "hard":
        num_of_attempts = 5

    while num_of_attempts != 0:
        print(f"You have {num_of_attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess > number_from_computer:
            print("Too high")
            num_of_attempts -= 1
        elif guess < number_from_computer:
            print("Too low")
            num_of_attempts -= 1
        elif guess == number_from_computer:
            print("Congratulations! You guessed the correct number")
            win = True
            break

        if num_of_attempts != 0:
            print("Guess again")

    if win:
        print("You win")
    else:
        print("Game over")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficult. Type 'easy' or 'hard': ")

guess_the_number(difficulty)