from art import logo
import random

def display_first(cards_player, score_player, cards_dealer):
    """This function show the initial display of the game"""
    print("===============================================")
    print(f"Your cards are: {cards_player}")
    print(f"Your score is {score_player}")
    print(f"The dealer cards are: [{cards_dealer[0]}, ?]")

def display_final(cards_player, score_player, cards_dealer, score_dealer):
    """This function show the final display of the game"""
    print("===============================================")
    print(f"Your cards are: {cards_player}")
    print(f"Your score is {score_player}")
    print(f"The dealer cards are: {cards_dealer}")
    print(f"The dealer score is {score_dealer}")

def blackjack_verificator(score_dealer, score_player):
    """This function check if has a blackjack in the beginning of the game"""
    if score_dealer == 21 and score_dealer != score_player:
        display_final(cards_player, score_player, cards_dealer, score_dealer)
        print("The dealer has a Blackjack, you lose :(")
        return True
    elif score_player == 21 and score_player != score_dealer:
        display_final(cards_player, score_player, cards_dealer, score_dealer)
        print("You have a blackjack! You win :D")
        return True
    elif score_player == 21 and score_dealer == 21:
        display_final(cards_player, score_player, cards_dealer, score_dealer)
        print("The dealer and you have a blackjack. It's a draw")
        return True
    else:
        return False

def ace_verificator(cards_parameter):
    """This function check if has aces in the cards player/dealer and change the value for 1 if it's necessary"""
    for card in cards_parameter:
        if card == 11 and sum(cards_parameter) > 21:
            return cards_parameter.index(card)


start = True

while start:
    print(f"{logo}")

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    game_over = False

    cards_player = [random.choice(cards)]
    cards_player.append(random.choice(cards))
    score_player = sum(cards_player)

    cards_dealer = [random.choice(cards)]
    cards_dealer.append(random.choice(cards))
    score_dealer = sum(cards_dealer)

    if blackjack_verificator(score_dealer, score_player) == False:

        display_first(cards_player, score_player, cards_dealer)

        another_card = input("Do you want another card? (y/n) ") == 'y'

        while another_card:
            cards_player.append(random.choice(cards))
            index = ace_verificator(cards_player)
            if index is not None:
                cards_player[index] = 1
            score_player = sum(cards_player)
            if score_player < 21:
                display_first(cards_player, score_player, cards_dealer)
                another_card = input("Do you want another card? (y/n) ") == 'y'
            elif score_player > 21:
                display_final(cards_player, score_player, cards_dealer, score_dealer)
                print("You went over. You lose :(")
                game_over = True
                break
            elif score_player == 21:
                display_final(cards_player, score_player, cards_dealer, score_dealer)
                print("You made 21 points! You win :D")
                game_over = True
                break
        
        while game_over == False:
            if score_dealer >= 17:
                if score_dealer > 21:
                    display_final(cards_player, score_player, cards_dealer, score_dealer)
                    print("The dealer went over. You win :D")
                    break
                elif score_dealer == 21:
                    display_final(cards_player, score_player, cards_dealer, score_dealer)
                    print("The dealer made 21 points! You lose :(")
                    break
                elif score_dealer == score_player:
                    display_final(cards_player, score_player, cards_dealer, score_dealer)
                    print("The dealer scores is equal to your. It's a draw")
                    break
                elif score_dealer > score_player:
                    display_final(cards_player, score_player, cards_dealer, score_dealer)
                    print("The dealer is close to 21 than you. You lose :(")
                    break
                elif score_player > score_dealer:
                    display_final(cards_player, score_player, cards_dealer, score_dealer)
                    print("You're is more close to 21 than dealer. You win :D")
                    break
            cards_dealer.append(random.choice(cards))
            index_2 = ace_verificator(cards_dealer)
            if index_2 is not None:
                cards_dealer[index_2] = 1
            score_dealer = sum(cards_dealer)
    start = input("Do you want to play another game of Blackjack? (y/n) ") == 'y'
 




