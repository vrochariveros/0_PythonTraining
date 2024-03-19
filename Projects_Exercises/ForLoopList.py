#Create a variable to store the given string "You can have data without information, but you cannot have information without data."
#Convert the given string to lowercase
#Create a list containing every lowercase letter of the English alphabet 

#for every letter in the alphabet list:
    #Create a variable to store the frequency of each letter in the string and assign it an initial value of zero
    #for every letter in the given string:
        #if the letter in the string is the same as the letter in the alphabet list
            #increase the value of the frequency variable by one.
    #if the value of the frequency variable does not equal zero:
        #print the letter in the alphabet list followed by a colon and the value of the frequency variable


quote = "You can have data without information, but you cannot have information without data.".lower() #Create a variable to store the given string "You can have data without information, but you cannot have information without data."

alphabet = "abcdefghijklmnopqrstuvwxyz" 
alphabetList = [] #Create a list containing every lowercase letter of the English alphabet 
for alphabetCharacter in "abcdefghijklmnopqrstuvwxyz":
  alphabetList.append(alphabetCharacter)

for alphabetCharacter in alphabetList: #for every letter in the alphabet list:
    characterFreq = 0 #Create a variable to store the frequency of each letter in the string and assign it an initial value of zero
    for letter in quote: #for every letter in the given string:
        if letter == alphabetCharacter: #if the letter in the string is the same as the letter in the alphabet list
            characterFreq = characterFreq + 1 #increase the value of the frequency variable by one.
    if characterFreq != 0:
        print(alphabetCharacter, ":", characterFreq)

