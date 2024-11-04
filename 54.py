class BasicDSA:
    def stringf(self):
        string = input("Enter a string: ")
        print("The reverse of the string is: ", string[::-1])
        print("The reverse words of the string is: ", string[::-1].split(" ")[::-1])
        return string[::-1]
    
    def stringwqoutes(self):
        string = input("Enter a string: ")
        string = '"' + string + '"' 
        return string

    def UpperLower(self):
        string = input("Enter a string: ")
        for elem in string:
            if ord(elem) >= 97 and ord(elem) <= 122:
                print(chr(ord(elem) - 32), end="")
            elif ord(elem) >= 65 and ord(elem) <= 90:
                print(chr(ord(elem) + 32), end="")
        return string
    
    def Encryption(self):
        string = input("Enter a string: ")
        for elem in string:
            if ord(elem) >= 97 and ord(elem) <= 122:
                print(self.EvenOddelem1(elem), end="")
            elif ord(elem) >= 65 and ord(elem) <= 90:
                print(self.EvenOddelem2(elem), end="")
        return string
    
    def EvenOddelem1(self,char):
        if ord(char)%2==0:
            return chr(ord(char)+7)
        else:
            return chr(ord(char)-7)
        
    def EvenOddelem2(self,char):
        if ord(char)%2==0:
            return chr(ord(char)+5)
        else:
            return chr(ord(char)-5)
    
    def Decryption(self,string):
        for elem in string:
            if ord(elem)>=97 and ord(elem)<=122:
                print(self.EvenOddelem3(elem),end="")
            elif ord(elem)>=65 and ord(elem)<=90:
                print(self.EvenOddelem4(elem),end="")
        return string
    
    def EvenOddelem3(self,char):
        if ord(char)%2==0:
            return chr(ord(char)-7)
        else:
            return chr(ord(char)+7)
        
    def EvenOddelem4(self,char):
        if ord(char)%2==0:
            return chr(ord(char)-5)
        else:
            return chr(ord(char)+5)

    def Uniquechar(self):
        string=input("Enter a string: ")
        string1=""
        L=[]
        for elem in string:
            if elem not in L:
                L.append(elem)
        for x in L:
            string1=string1+str(x)
        return string1
    def shuffle(self):
        string=input("Enter a string: ")
        L1=list(string)
        L2=[None]*len(L1)
        for i in range(0,len(L1),2):
            if i+1<len(L1):
                L2[i+1]=L1[i]
            else:
                L2[i]=L1[i]
        for i in range(1,len(L1),2):
            L2[i-1]=L1[i]
        string1="".join(elem for elem in L2 if elem is not None)
        return string1
    
    def addstrtostartnend(self):
        string1=input("Enter a string: ")
        string2=input("Enter another string: ")
        if len(string1)>len(string2):
            return string2+string1+string2
        elif len(string1)<len(string2):
            return string1+string2+string1
        else:
            return "Same length"
obj=BasicDSA()
print(obj.addstrtostartnend())

