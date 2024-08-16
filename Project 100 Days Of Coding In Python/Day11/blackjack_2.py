from art import logo
import random

def score(gamester):
    return sum(gamester)

def black_jack_verificator(gamester_score):
    if gamester_score == 21:
        print("There's a blackjack in the game!")
        return True
    
def select_cards(gamester_cards):
    gamester_cards += [random.choice(cards)]

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
player = []
computer = []

for x in range(2):
    select_cards(player)
    select_cards(computer)

if black_jack_verificator(score(player)):
    print("The player win")
elif black_jack_verificator(score(computer)):
    print("The computer win")





    
