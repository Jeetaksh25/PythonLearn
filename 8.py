import math
c=0
while c==0:
    n=float(input("Enter a number: "))
    if n>0:
        print(math.pow(n,2))
        c=1

    elif n<0:
        print("The value is negative")
        c=0
    else:
        print("Zero")
        c=0