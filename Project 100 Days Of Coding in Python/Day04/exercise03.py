import random

print("========== Rock, Paper and Scissors ==========")
your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ").strip()
while your_choice != "0" and your_choice != "1" and your_choice != "2":
    print("Invalid input, please insert correctly")
    your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

match your_choice:
    case "0":
        your_choice = rock
        print(your_choice)
    case "1":
        your_choice = paper
        print(your_choice)
    case "2":
        your_choice = scissors
        print(your_choice)

game = [rock, paper, scissors]
computer_choice = random.choice(game)
print("Computer chose:")
print(computer_choice)

if (your_choice == rock and computer_choice == scissors) or (your_choice == paper and computer_choice == rock) or (your_choice == scissors and computer_choice == paper) :
    print("You win")
elif (your_choice == rock and computer_choice == paper) or (your_choice == paper and computer_choice == scissors) or (your_choice == scissors and computer_choice == rock):
    print("You lose")
else:
    print("Drawn game")


