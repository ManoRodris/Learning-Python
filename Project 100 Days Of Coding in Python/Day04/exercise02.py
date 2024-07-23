line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

move = input("Enter your move using A, B and C for columns and 1, 2 and 3 for rows (example: A2, B3): ").lower()
while (move[0] != 'a') and (move[0] != 'b') and (move[0] != 'c'):
    while (move[1] != '1') and (move[1] != '2') and (move[1] != '3'):
        print("Invalid input, please insert correctly")
        move = input("Enter your move using A, B and C for columns and 1, 2 and 3 for rows (example: A2, B3): ").lower()

if move == 'a1':
    map[0][0] = "X"
elif move == 'a2':
    map[1][0] = "X"
elif move == 'a3':
    map[2][0] = "X"
elif move == 'b1':
    map[0][1] = "X"
elif move == 'b2':
    map[1][1] = "X"
elif move == 'b3':
    map[2][1] = "X"
elif move == 'c1':
    map[0][2] = "X"
elif move == 'c2':
    map[1][2] = "X"
elif move == 'c3':
    map[2][2] = "X"

print(f"{line1}\n{line2}\n{line3}")