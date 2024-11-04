v=0
while v==0:
    x=str(input("Enter an Alphabet or Number: "))
    y=ord(x)
    if y>=97 and y<=122:
        print("Lowercase")
        v=1
    elif y>=65 and y<=90:
        print("Uppercase")
        v=1
    elif y>=48 and y<=57:
        print("Its a number")
        v=1
    else:
        print("Its a special character")
        print("Enter again")
        v=0