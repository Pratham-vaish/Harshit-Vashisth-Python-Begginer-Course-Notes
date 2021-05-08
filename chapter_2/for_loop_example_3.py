name = input("Enter you name.. ")
NAME = name.lower()
temp = " "
for i in range(len(name)):
    if NAME[i] not in temp:
        print(f"Frequency of {NAME[i]} is {NAME.count(NAME[i])}")
        temp += NAME[i]
        
    