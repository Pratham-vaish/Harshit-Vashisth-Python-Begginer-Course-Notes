def fibo(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        for i in range(n-2):
            print(a, b, end=" ")
            c = a+b
            a = b
            b = c
            print(b, end=" ")
d = int(input("Enter the number till which you want the series: "))
print(fibo(d))
            