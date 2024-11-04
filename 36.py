def SumOSq(n,m):
    sum1=0
    sum2=0
    n=str(n)
    m=str(m)
    for i in n:
        sum1+=int(i)**2
    for i in m:
        sum2+=int(i)**2
    x = sum1-sum2
    if x<0:
        print("N")
    elif x>0:
        print("P")
    elif x==0:
        print("Z")
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
SumOSq(num1,num2)