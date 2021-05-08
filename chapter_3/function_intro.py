# functions are used so we have to not right code again 
# to assign a fun it starts with def
# len is a build in function
# name = pratham
# print("len(pratham) ") 

import random
def any(a,b):
    return random.randint(a,b)

a = int(input("Enter first number : "))
b = int(input("Enter second number :"))
print(any(a,b))