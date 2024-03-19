quote = "You can have data without information, but you cannot have information without data.".lower()
alphabet = "abcdefghijklmnopqrstuvwxyz" 


for alphabetCharacter in alphabet:
    characterFreq = 0
    for letter in quote:
        if alphabetCharacter == letter: 
            characterFreq = characterFreq + 1 
    if characterFreq != 0:
        print(alphabetCharacter, ":", characterFreq)

        
       


