from art import logo
import os

print(logo)
print("Welcome to the secret auction!")
auction_dictionary = {}
other_bids = True

while other_bids:
    name_key = input("Your name: ")
    bid_value = int(input("Your bid: $"))
    auction_dictionary[name_key] = bid_value
    other_bids = input("Are there any other bidders (yes/no)? ").lower().strip() == "yes"
    os.system('cls')

def winner_seeker(dictionary):
    highest_bid = 0
    winner_auction = ""
    for key in dictionary:
        if dictionary[key] > highest_bid:
            highest_bid = dictionary[key]
            winner_auction = key
    print(f"The winner is {winner_auction} with a bid of ${highest_bid}")

winner_seeker(auction_dictionary)