till = int(input(" Enter the number till which you want the sum:  "))
total = 0
for i in range(1, till+1):
    total += i
print(f"Sum of all the numbers till, {till} is {total} ")