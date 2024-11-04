def StringSearch(Istr,Schar):
    x=0
    for i in range(len(Istr)):
        if Istr[i]==Schar:
            x=i
        else:
            x=-1
    if x==-1:
        print(f"{Schar} not found in {Istr}")
    else:
        print("The position of the character is: ",x+1)

x=input("Enter a string: ")
y=input("Enter a character to search in the given string: ")
StringSearch(x,y)
