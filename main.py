#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    l = letter.read()
    with open("./Input/Names/invited_names.txt") as user_names:
        names = user_names.read().splitlines()
        print(names)
        for name in names:
            with open(f"./Output/letter_for_{name}.txt", mode="w") as r:
                r.write(l.replace("[name]", f"{name}"))
