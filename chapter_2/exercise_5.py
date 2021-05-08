name = (input("Enter your name .. ")).lower()
i = 0
while i < len(name):
    print(f"frequency of {name[i]} is {name.count(name[i])}")
    i += 1
print("here is your answer")