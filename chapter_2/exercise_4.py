a = input("Enter the series of number")
b = len(a) - 1
i = 0
total = 0
while i <= b:
    total += int(a[i])
    i += 1
print(f"Sum of the series, {a} is {total} ")
    