a = input("Enter the series of number: ")
b = len(a)
total = 0
for i in range(b):
    total += int(a[i])
print(total)