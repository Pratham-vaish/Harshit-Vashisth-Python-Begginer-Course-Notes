# Function to return last character
name = input("Enter your name: ")
def last(name):
    return name[-1]
print(last(name))

# function to return odd or even

def odd_even(a):
    if a%2 == 0 :
        return  "even"
    return "odd"
a = int(input("Enter the number: "  ))
print(odd_even(a))

# Function to check odd even in shorter way 

def is_even(a):
    return a%2 == 0

print(is_even(a))

