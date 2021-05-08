# to check string is empty or not
name = input("Enter your name.. ")
name = name.replace(" ", "")
if name:
    print(f"Your name is {name} ")
else:
    print(" you didn't type anything")