Str1=input("Enter a string: ")
for elem in Str1:
    if ord(elem)>=65 and ord(elem)<=90:
        Str1=Str1.replace(elem,chr(ord(elem)+32))
    elif ord(elem)>=97 and ord(elem)<=122:
        Str1=Str1.replace(elem,chr(ord(elem)-32))
print(Str1)
        