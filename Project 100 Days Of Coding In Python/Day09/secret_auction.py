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


the_highest_bid = max(auction_dictionary.values())
the_auction_winner = max(auction_dictionary, key=lambda k:auction_dictionary[k])

print(f"The winner is {the_auction_winner} with a bid of ${the_highest_bid}")