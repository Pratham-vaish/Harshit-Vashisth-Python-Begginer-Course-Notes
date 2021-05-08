a = int(input("Which table do you want... "))
b = int(input("Till which number... "))
i = 1
while i <= b:
    print(f" {a} X {i} is {a*i} ")
    i = i + 1
print(f"Here is your table of {a}")
input("Press enter key to close")