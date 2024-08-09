def gameboard():
    print("======== Tic-Tac-Toe ========\n")

    line1 = ["⬜️","️⬜️","️⬜️"]
    line2 = ["⬜️","⬜️","️⬜️"]
    line3 = ["⬜️️","⬜️️","⬜️️"]

    play = [line1, line2, line3]

    print(f"{line1}\n{line2}\n{line3}")

def menu():
    move = input("Enter your move using A, B and C for columns and 1, 2 and 3 for rows (example: A2, B3): ").lower()
    while (move[0] != 'a') and (move[0] != 'b') and (move[0] != 'c'):
        while (move[1] != '1') and (move[1] != '2') and (move[1] != '3'):
            print("Invalid input, please insert correctly")
            move = input("Enter your move using A, B and C for columns and 1, 2 and 3 for rows (example: A2, B3): ").lower()


gameboard()

menu()


