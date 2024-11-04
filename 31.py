def PerfectSquare(n):
    for i in range(1,n+1):
        if i*i==n:
            return True,i
    return False
num=int(input("Enter a number: "))
if PerfectSquare(num):
    print(num,f"is a perfect square of {PerfectSquare(num)[1]}")
else:
    print(num,"is not a perfect square")