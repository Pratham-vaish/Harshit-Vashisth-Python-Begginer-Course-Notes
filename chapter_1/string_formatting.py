name = "pratham"
age = 14
#How we normally print
print("hello " + name + " your age is " + str(age)) #UGLY, UNCLEAN AND HARD

#String formatting makes it easy

#python 3
print("hello {} your age is {}".format(name, age)) #cleaner and easier

#python 3.6
print(f"hello {name} your age is {age}") #very simple and clean

# You dont need to worry about str and int you can also add things written in {}

print(f"After two years your age will be {age+2} ")