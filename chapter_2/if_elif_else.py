name = input("PLEASE ENTER YOUR NAME.. ")
age = int(input("PLEASE ENTER YOUR AGE... "))
if age <= 3:
    print(f"Ticket fee for you baby {name} if FREE!!!")
elif age <= 14:
    print(f"Ticket fee for you kid {name} is 250rs. ")
elif age <= 60:
    print(f"Ticket fee for you sir {name} is 300rs ")
else:
    print(f"Ticket fee for you Uncle {name} is FREE!! ")
input("Press Enter key to close..")
