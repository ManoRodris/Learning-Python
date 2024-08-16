from art import logo

def caeser(message, shift_amount, chosen_direction):
    end_text = ""
    for i in range(len(message)):
        if message[i] in alphabet:
            index = alphabet.index(message[i])
            if chosen_direction == 'encode':
                index_letter = (index + shift_amount) % 26
            elif chosen_direction == 'decode':
                index_letter = (index - shift_amount) % 26
            letter = alphabet[index_letter] 
            end_text += letter
        else:
            end_text += message[i]
    print(f"The {chosen_direction}d text is: {end_text}")

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = 'yes'

while restart != 'no':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    while direction != 'encode' and direction != 'decode':
        print("Wrong answer, please insert a correct input between 'encode' or 'decode'")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caeser(message=text, shift_amount=shift, chosen_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")
    while restart != 'yes' and restart != 'no':
        print("Wrong answer, please insert a correct input between 'yes' or 'no'")
        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")
