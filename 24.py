import random
def listS(L):
    element=input("Enter element to be searched:")
    if element in L:
        x=L.index(element)
        print(f"Element found at index {x+1} ")
        breakpoint
    else:
        print("Element not found")
def listCnS():
    L=[]
    nE=int(input("Enter number of elements:"))
    for i in range(nE):
        L.append(input(f"Enter element #{i+1}:"))
    print(L)
    ch1=int(input("Enter 1 to search an element or 0 to exit:"))
    if ch1==1:
        listS(L)
    else:
        breakpoint
    return L
def RandomList():
    L=[]
    nE=int(input("Enter number of elements:"))
    for i in range(nE):
        x=random.randint(65,122)
        L.append(chr(x))
    print(L)

def L1L2L3():
    L1=listCnS()
    L2=[]
    L3=[]
    for elem in L1:
        if int(elem)%2==0:
            L2.append(elem)
        else:
            L3.append(elem)
    print(L2)
    print(L3)

C1=int(input("Enter 1 for self list creation and 2 for random list creation and 3 for L1L2L3:"))
if C1==1:
    listCnS()
elif C1==2:
    RandomList() 
elif C1==3:
    L1L2L3()  
