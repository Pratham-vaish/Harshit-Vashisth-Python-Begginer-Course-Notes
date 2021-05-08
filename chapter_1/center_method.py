#center method is used to put any symbol in starting ad ending of a string
print("This program can center your name with any character")
print("Things you have to input :- YOUR NAME,CHARACTER,FREQUENCY")
name, x, y = input('enter your name, the character and how many times :  ').split(",")
print(name.center(len(name)+int(y), x)) 