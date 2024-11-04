x=int(input("Enter the number for last digit:"))
y=int(input("Enter the number for first digit:"))
L1=x%10
v=str(y)
L2=y//(10**(len(v)-1))
print(L1)
print(L2)