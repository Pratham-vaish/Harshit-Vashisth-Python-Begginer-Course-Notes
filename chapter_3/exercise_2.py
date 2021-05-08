word = input("Enter a Palindrom word ")
word = word.lower()
reversed_word = word[::-1]
if reversed_word == word :
    print("Yes, it is a Palindrom")
else:
    print('NO, its not a Palindrom')
input("Press enter to close")


