def check(a,b,c):
    if a > b and a > c :
        return f"{a} is bigger than {b} and {c} "
    elif b > a and b > c :
        return f"{b} is bigger than {a} and {c} "
    else:
        return f"{c} is bigger than {a} and {b} "
    

a, b, c = input("Enter three no. with comma: ").split(",")
int(a) , int(b) , int(c)
print(check(a,b,c))