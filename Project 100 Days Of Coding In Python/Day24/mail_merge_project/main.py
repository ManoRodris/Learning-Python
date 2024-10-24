#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as invited_names:
    names_with_space = invited_names.readlines()
    names = [all_names.strip("\n") for all_names in names_with_space]

with open("./Input/Letters/starting_letter.txt", "r+") as letter:
    new_letter = letter.read()
    for each_name in names:
        with open(f"./Output/ReadyToSend/letter_for_{each_name}.txt", "w") as new_letters:
            letter_replaced = new_letter.replace("[name]",f"{each_name}")
            new_letters.write(letter_replaced)


