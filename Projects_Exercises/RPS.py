#import function randint to randomize:
#from module import function
from random import randint 

#list
options = ["ROCK", "PAPER", "SCISSORS"]

#create dictionary with three value pairs
#define message variable with values inside of it (tie, won, lost)
message = {
  "tie": "Lol, it's a tie",
  "won": "Nice one, you won!", 
  "lost": "Lol, you lose"
}

#define function that decides winner
#def
def decide_winner(user_choice, computer_choice):
    print ("You chose: %s" % user_choice)
    print ("G0BL1IN chose: %s" % computer_choice)
    if  user_choice == computer_choice:
        print(message["tie"])
    elif user_choice == options[0] and computer_choice == options[2]:
        print (message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print (message["won"])
    elif user_choice == options[2] and computer_choice == options[1]:
        print (message["won"])
    else:
        print (message["lost"])
    
#store user input: input
def play_RPS():
    user_choice = input("Enter Rock, Paper, or Scissors: ")
    user_choice = user_choice.upper()
    #randint function randomizes variables
    #randint(0, 2) will return an integer that’s either 0, 1, or 2. 
    #The item in options at this random integer index will be either "ROCK", "PAPER", or "SCISSORS".
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)

#variable will determine if program should be running or not 
isRunning = True

while isRunning == True:
    
    play_RPS()
    
    userContinue = input("Another round? Type Y for yes N for no: ").lower()
    if userContinue == 'n':
        isRunning = False

print("Okay, see ya later")

