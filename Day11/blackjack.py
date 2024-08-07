from art import logo
import random

def display_first(cards_player, score_player, cards_dealer):
    print(f"Your cards are: {cards_player}")
    print(f"Your score is {score_player}")
    print(f"The dealer cards are: [{cards_dealer[0]}, ?]")

def display_final(cards_player, score_player, cards_dealer, score_dealer):
    print(f"Your cards are: {cards_player}")
    print(f"Your score is {score_player}")
    print(f"The dealer cards are: {cards_dealer}")
    print(f"The dealer score is: {score_dealer}")

def blackjack_verificator(score_dealer, score_player):
    if score_dealer == 21:
        display_final(cards_player, score_player, cards_dealer, score_dealer)
        print("The dealer has a Blackjack, you lose :(")
        #break
    elif score_player == 21:
        display_final(cards_player, score_player, cards_dealer, score_dealer)
        print("You have a blackjack! You win :D")
        #break

def ace_verificator(cards_parameter, ace_parameter):
    for card in cards_parameter:
        if card == 11 and sum(cards_parameter) > 21:
            card = 1
            if card == 1 and sum(cards_parameter) > 21:
                ace_parameter = True


start = input("Do you want to play a game of Blackjack? (y/n) ") == 'y'
print(f"{logo}")

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
ace_busted = False

cards_player = [random.choice(cards)]
cards_player.append(random.choice(cards))
score_player = sum(cards_player)

cards_dealer = [random.choice(cards)]
cards_dealer.append(random.choice(cards))
score_dealer = sum(cards_dealer)

blackjack_verificator(score_dealer, score_player)

display_first(cards_player, score_player, cards_dealer)

another_card = input("Do you want another card? (y/n) ") == 'y'

while another_card:
    cards_player.append(random.choice(cards))
    score_player = sum(cards_player)
    ace_verificator(cards_player, ace_busted)
    if score_player < 21:
        display_first(cards_player, score_player, cards_dealer)
        another_card = input("Do you want another card? (y/n) ") == 'y'
    elif score_player > 21:
        display_final(cards_player, score_player, cards_dealer, score_dealer)
        print("You went over. You lose :(")
        break
    elif score_player == 21:
        display_final(cards_player, score_player, cards_dealer, score_dealer)
        print("You have a blackjack! You win :D")
        break

 




