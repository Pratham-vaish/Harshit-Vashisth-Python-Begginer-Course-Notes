#how to take two two inputs in one line 
name, age = input('Enter your name and age: ').split()
print( name +" "+ age)
# .split func is used to seprate two input
# we can change backspace with comma or any other symbol
standard, roll_no = input("ENTER YOUR CLASS AND ROLL NO. WITH COMMA:... " ).split(",")
print('You study in s' + str(standard) + "and your roll no. is " + roll_no )