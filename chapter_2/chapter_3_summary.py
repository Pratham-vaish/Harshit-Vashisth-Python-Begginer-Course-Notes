# name = input("Enter your name: ")
# if name == "pratham" or name == "Pratham":
#     print("you are pratham")
# elif name == 'PAYAL' or len(name) == 5:
#     print("Your ar Payal")
# else:
#     print("I don't know you")               
    
import random
winning_number = random.randint(1,100)
guess = 0
while True:
    guessed_number =  int(input("Guess a number between 1 to 100 : "))
    if guessed_number == winning_number:
       print(f"\nYes, you won in {guess} guesses")
       break
    else:
        if guessed_number > winning_number:
            print("\nToo high, guess again ")    
        else :
            print("\nToo low, guess again ")
        guess += 1
        continue    
