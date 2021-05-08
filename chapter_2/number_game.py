import random
winning_number = random.randint(1,100)

print("WELCOME \nThis is a number Guessing game \nYou have to Guess between 1 to 100 ")
guessed_number = int(input("You can guess again but you have only 10 chances \nGuess the number.. "))
guess = 0
print("\n")
for guess in range(10) :
    if guessed_number == winning_number:
        if guess > 0:
            print(f"Yes, you won in {guess} tries ")
        else:
            print("OMG!! You won only in one try")
        break
    else:
        if guess == 8:
            print("OOO! its your last try, GUESS IT RIGHT OR GAME OVER!!!")
        elif guessed_number > winning_number:
            print("Too high, try again ")
        else:
            print("Too low, try again ")
        guessed_number = int(input("Guess again: "))
        guess += 1
        print("\n")

            
if guess == 10:
    print("Sorry GAME OVER, Chances are over  ")
    print("\n")
else :
    pass
print("Thank you for playing \n MADE BY PRATHAM ")
input("Press enter to close")