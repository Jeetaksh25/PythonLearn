def Ascend(L,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if(L[j]>L[j+1]):
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp

def Descend(L,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if(L[j]<L[j+1]):
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp

C1=int(input("Enter number of elements for List: "))
L1=[]
for i in range(C1):
    L1.append(int(input(f"Enter element #{i+1}: ")))
print(L1)

C2=int(input("Enter 1 for ascending order or 2 for descending order: "))
if C2==1:
    Ascend(L1,C1)
    print(L1)
elif C2==2:
    Descend(L1,C1)
    print(L1)