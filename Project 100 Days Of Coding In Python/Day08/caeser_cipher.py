def encrypt (message, switch):
    cipher_text = ""
    for i in range(len(message)):
        if message[i] in alphabet:
            index = alphabet.index(message[i])
            index_letter = (index + switch) % 26
            letter = alphabet[index_letter] 
            cipher_text += letter
        else:
            cipher_text += message[i]
    print(f"The encoded text is: {cipher_text}")

def decrypt (message, switch):
    cipher_text = ""
    for i in range(len(message)):
        if message[i] in alphabet:
            index = alphabet.index(message[i])
            index_letter = (index - switch) % 26
            letter = alphabet[index_letter] 
            cipher_text += letter
        else:
            cipher_text += message[i]
    print(f"The decoded text is: {cipher_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
while direction != 'encode' and direction != 'decode':
    print("Wrong answer, please insert a correct input")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))
while shift <= 0 and shift > 26:
    print("Wrong answer, please insert a correct input between 0 and 26")
    shift = int(input("Type the shift number:\n"))

match direction:
    case 'encode':
        encrypt(message=text, switch=shift)
    case 'decode':
        decrypt(message=text, switch=shift)