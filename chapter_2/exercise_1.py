import random
winning_number = random.randint(10,20)
guessed_number = int(input("Guess a number between 10 to 20... "))
if winning_number == guessed_number:
    print("Yes, you won")
else:
    print("you lose")
    if winning_number <= guessed_number:
        print("Your number was too high")
    else:
        print("Your number was too low")
print("the winning number was" +" "+ str(winning_number))
input("press any key to close")

