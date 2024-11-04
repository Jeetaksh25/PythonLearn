def is_Armstrong(n):
    total=0
    L=len(str(n))
    if n>0:
        r=n%10
        total=total+(r**L)
        n=n//10
        is_Armstrong(n)
    return total

original=int(input("Enter the number: "))
if original==is_Armstrong(original):
    print(f"{original} is an Armstrong number")
else:
    print(f"{original} is not an Armstrong number")