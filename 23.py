def NeonNo(n):
    sum=0
    x=str(n)
    for digit in x:
        sum+=int(digit)
    return sum**2==n

n=int(input("Enter a number to check for Neon: "))
if NeonNo(n):
    print(f"{n} is a Neon Number !!!")
else:
    print(f"{n} is not a Neon Number :(")