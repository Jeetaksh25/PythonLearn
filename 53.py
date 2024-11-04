import random
import algorithm
import string

class RandomFunc:
    def RandomNo(self):
        n=int(input("Enter range of numbers: "))
        rand=random.randint(1,n)
        print(rand)
        return rand
    def RandomChar(self):
        string=input("Enter a string: ")
        rand=random.choice(string)
        print(rand)
        return rand
    
    def RandomList(self):
        L=list(map(int,input("Enter numbers: ").split(" ")))
        rand=random.choice(L)
        print(rand)
        return rand
    
    def OTP(self):
        length=int(input("Enter length of OTP: "))
        s=""
        for i in range(length):
            s=s+str(random.randint(0,9))
        print(int(s))
        return int(s)
    
    def SeedGen(self):
        L=list(map(int,input("Enter numbers: ").split(" ")))
        for i in L:
            random.seed(i)
            print(random.randint(1,100))
        
    def Sample(self):
        L=list(map(int,input("Enter numbers: ").split(" ")))
        sample=random.sample(L,3)
        print(sample)
        return sample
    

class SquareRoot_Product:
    def Product(self,x,y):
        return x*y
    def SquareRoot(self,x):    
        while True:
            if(x<0):
                return 0
            y=x
            z=(y+(x/y))/2
            while(abs(y-z)>0.000001):
                y=z
                z=(y+(x/y))/2
            return z


class DataStructure:
    def alphabets(self):
        laplpha=list(string.ascii_lowercase)
        return laplpha
    def Raplphabets(self,list):
        random.shuffle(list)
        return list
    
    def Password(self):
        length=int(input("Enter length of password: "))
        lalpha=list(string.ascii_lowercase)
        Calpha=list(string.ascii_uppercase)
        num=list(string.digits)
        symbol=list(string.punctuation)
        L=[]
        len_for_lalpha=random.randint(1,length-3)
        len_for_Calpha=random.randint(1,length-len_for_lalpha-2)
        len_for_num=random.randint(1,length-len_for_lalpha-len_for_Calpha-1)
        len_for_symbol=random.randint(1,length-len_for_lalpha-len_for_Calpha-len_for_num)
        for i in range(len_for_lalpha):
            L.append(random.choice(lalpha))
        for i in range(len_for_Calpha):
            L.append(random.choice(Calpha))
        for i in range(len_for_num):
            L.append(random.choice(num))
        for i in range(len_for_symbol):
            L.append(random.choice(symbol))
        random.shuffle(L)
        L.sort()
        print("".join(L))
        return "".join(L)
    
    def Remove_all_occurences(self):
        L=list(map(str,input("Enter elements: ").split(" ")))
        Selem=input("Enter the element to be removed: ")
        while Selem in L:
            L.remove(Selem)
        L=[elem for elem in L if elem!=" "]
        print(L)
        return L
    

obj=DataStructure()
obj.Password()