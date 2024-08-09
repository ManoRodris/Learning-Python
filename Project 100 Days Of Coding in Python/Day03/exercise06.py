print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
direccion = input("You're at a cross road. Where do you want to go? (left/right)\n").lower().strip() == 'left'
if direccion == True:
    direccion_2 = input("You've come to a lake. There is an Island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swin across\n").lower().strip() == 'swim'
    if direccion_2 == True:
        direccion_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower().strip()
        match direccion_3:
            case "red":
                print("Wrong answer, you're burned by fire, pay more attention in the next time!")
            case "blue":
                print("Wrong answer, you're was eaten by beasts, pay more attention in the next time!")
            case "yellow":
                print("You found the treasure, congratulations!")
    else:
        print("Wrong answer, you get attacked by a angry trout, pay more attention in the next time!")
else:
    print("Wrong answer, you fell into a hole, pay more attention in the next time!")
