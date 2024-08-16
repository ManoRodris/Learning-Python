import random

print("======== Flip a coin ========")
your_choice = input("Heads or Tails: ")
while your_choice != "Heads" and your_choice != "Tails":
    print("Invalid input, please insert correctly")
    your_choice = input("Heads or Tails: ")

random_number = random.randint(0,1)

computer_choice = ["Heads", "Tails"]

if computer_choice[random_number] == your_choice:
    print("Congratulations! You win, the computer chose " + computer_choice[random_number])
else:
    print("Sorry, you lost, the computer chose " + computer_choice[random_number])