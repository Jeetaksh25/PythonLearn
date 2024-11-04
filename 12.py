#this code is to print the last digit of a three digit number
a=input("Enter a three digit number: ")
lst=list(a)
for i in range(-1,-4,-1):
    print(lst[i],end=" ")
x=int(a)%10
print(" ")   
print(x)