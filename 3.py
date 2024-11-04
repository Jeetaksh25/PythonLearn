c1=int(input("Enter 1 to open calculator, 2 to view last result and 3 to exit: "))
while c1!=3:
    if c1==1:
        print("*********Calculator*********")
        print("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for factorial, 6 for exponential: ")
        c2=int(input())
        if c2==1:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            result=a+b
        elif(c2==2):
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            result=a-b
        elif(c2==3):
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            result=a*b
        elif(c2==4):
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            result=a/b
        elif(c2==5):
            a=int(input("Enter number: "))
            result=1
            for i in range(1,a+1):
                result=result*1
        elif(c2==6):
            a=int(input("Enter number for base: "))
            b=int(input("Enter number for power: "))
            result=a**b
        print(result)

        c1=int(input("Enter 1 to open calculator, 2 to view last result and 3 to exit: "))

    elif c1==2:
        print(result)

    elif c1==3:
        break    