from art import logo, vs
from random import choice
from celebrities import data
from os import system

def choose_celebrity(first_celebrity):
    """Chooses the second celebrity, excluding the possibility of the second celebrity be the same as the first celebrity"""
    second_data = [x for x in data if x != first_celebrity]
    second_celebrity = choice(second_data)
    return second_celebrity

def comparator_of_celebrities(guess, first_celebrity, second_celebrity):
    """Compares the guess of the user with the follower count of each celebrity"""
    if guess == "a":
        if first_celebrity["follower_count"] > second_celebrity["follower_count"]:
            return True
        else:
            return False
    elif guess == "b":
        if second_celebrity["follower_count"] > first_celebrity["follower_count"]:
            return True
        else:
            return False

celebrity_a = choice(data)
celebrity_b = choose_celebrity(celebrity_a)
game_over = False
score = 0

print(logo)

while game_over == False:
    print(f"Compare A: {celebrity_a["name"]}, a {celebrity_a["description"]} from {celebrity_a["country"]}")
    print(vs)
    print(f"Against B: {celebrity_b["name"]}, a {celebrity_b["description"]} from {celebrity_b["country"]}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
    
    if comparator_of_celebrities(guess, celebrity_a, celebrity_b):
        system("cls")
        print(logo)
        score += 1
        print(f"You're right! Current score {score}")
        to_compare_celebrities = celebrity_a
        celebrity_a = celebrity_b
        celebrity_b = choose_celebrity(celebrity_a)
        while celebrity_b == to_compare_celebrities:
            if celebrity_b == to_compare_celebrities:
                celebrity_b = choose_celebrity(celebrity_a)
    else:
        system("cls")
        print(logo)
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")

    


