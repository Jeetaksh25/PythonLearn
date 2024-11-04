a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=int(input("Enter another number:"))
if a<b:
    small1=a
else:
    small1=b
if small1>c:
    small=small1
else:
    small=c
print(small)