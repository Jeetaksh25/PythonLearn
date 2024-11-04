import string
class Recursion:
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)

    def lcm(self,a,b):
        return abs(a*b)//self.gcd(a,b)

    def factorial(self,a):
        if a==0:
            return 1
        return a*self.factorial(a-1)

    def fibonacci(self,n):
        if n<=1:
            return n
        return self.fibonacci(n-1)+self.fibonacci(n-2)

    def sum_of_digits(self,n):
        if n==0:
            return 0
        return n%10 + self.sum_of_digits(n//10)


    def sqrt(self,n):
        y=n
        z=(y+(n/y))/2
        while(abs(y-z)>=0.00001):
            y=z
            z=(y+(n/y))/2
        return z

    def power(self,a,b):
        if b==0:
            return 1
        return a*self.power(a,b-1)

    def cube_of_even(self,n):
        L=[]
        for i in range(n+1):
            if i%2==0:
                L.append(i**3)
        x=sorted(set(L))
        return x

def main1():
    while 1==1:
        Choice=int(input("Enter 1 for GCD, 2 for LCM, 3 for Factorial, 4 for Fibonacci, 5 for Sum of digits, 6 for Square root, 7 for Power, 8 for Cube of even numbers: "))
        if Choice==1:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(Recursion().gcd(a,b))
        elif Choice==2:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(Recursion().lcm(a,b))
        elif Choice==3:
            a=int(input("Enter number: "))
            print(Recursion().factorial(a))
        elif Choice==4:
            a=int(input("Enter number: "))
            print(Recursion().fibonacci(a))
        elif Choice==5:
            a=int(input("Enter number: "))
            print(Recursion().sum_of_digits(a))
        elif Choice==6:
            a=int(input("Enter number: "))
            print(Recursion().sqrt(a))
        elif Choice==7:
            a=int(input("Enter number: "))
            b=int(input("Enter power: "))
            print(Recursion().power(a,b))
        elif Choice==8:
            a=int(input("Enter number: "))
            print(Recursion().cube_of_even(a))

class Unit4:
    def reverse_string(self):
        s=input("Enter a string: ")
        print(s[::-1])

    def reverse_words(self):
        s=input("Enter a sentence: ")
        L=s.split(" ")
        L.reverse()
        print(" ".join(L))

    def anagrams(self):
        s1=input("Enter string1: ").lower()
        s2=input("Enter string2: ").lower()
        L1=sorted(list(s1))
        L2=sorted(list(s2))
        print(L1)
        print(L2)
        return L1==L2

    def longest_word(self):
        s=input("Enter a sentence: ")
        L1=list(map(str,s.split(" ")))
        Len=[]
        for elem in L1:
            Len.append(len(elem))
        dictionary=dict(zip(L1,Len))
        print(dictionary)
        x=max(dictionary, key=dictionary.get)
        print(x)

    def Capitalize_sentence(self):
        s=input("Enter a sentence: ")
        L=list(s)
        L[0]=L[0].upper()
        for i in range(len(L)-2):
            if L[i] in string.punctuation and L[i+1]==" ":
                L[i+2]=L[i+2].upper()  
        print("".join(L))

    def first_unique_char(self):
        s=input("Enter a string: ")
        L=list(s)
        for i in range(len(L)):
            if L.count(L[i])==1:
                print(L[i])
                break
        else:
            print(-1)

    def compress_string(self):
        s=input("Enter a string: ")
        L=list(s)
        L2=[]
        result=[]
        for i in range(len(L)):
            if L[i] not in L2:
                L2.append(L[i])
        for elem in L2:
            result.append(str(elem)+str(L.count(elem)))
        print("".join(result))

    def frequency_sort(self):
        s=input("Enter a string: ")
        L=list(s)
        L2=[]
        L3=[]
        T=tuple()
        resultS=str("")
        for elem in L:
            if elem not in L2:
                L2.append(elem)
        for elem in L2:
            L3.append(L.count(elem))
        Tuple=tuple(zip(L2,L3))
        Tuple=sorted(Tuple, key=lambda x: x[1], reverse=True)
        print(Tuple)
        for i,j in Tuple:
            resultS=resultS+i*j
        print(resultS)

    def dictionary_of_evencubes(self):
        Keys=[]
        Values=[]
        num=int(input("Enter a number: "))
        for i in range(1,num+1):
            if i%2==0:
                Keys.append(i) 
                Values.append(i**3)
        print(dict(zip(Keys,Values)))

    def vowel_transform(self):
        s=input("Enter a string: ")
        vowels={"a":"e","e":"i","i":"o","o":"u","u":"a","A":"E","E":"I","I":"O","O":"U","U":"A"}
        L=list(s)
        for elem in L:
            if elem in vowels:
                L[L.index(elem)]=vowels[elem]
        print("".join(L))
    
    def hashtag_extractor(self):
        s=input("Enter a sentence: ")
        L=list(map(str,s.split(" ")))
        L2=[]
        for elem in L:
            list(elem)
            if elem[0]=="#":
                L2.append(elem)

        print(" ".join(L2))
    
    def set_operation(self):
        set1={1,2,3}
        set2={1,2,3,4}
        print(set1.issubset(set2))

    def tuple_swap(self):
        t1=(1,2,3)
        t=(t1[0],)
        t2=tuple(reversed(t1[1:]))
        t3=t+t2
        print(t3)

    def update_dictionary(self):
        d1={"a":1,"b":2,"c":3}
        d1.update({"b":4})              
        print(d1)           
    
    def count_tuple_elem(self):
        t=tuple(map(int,input("Enter a tuple: ").split(",")))
        L=list(t)
        Lu=[]
        countL=[]
        for i in L:
            if i not in Lu:
                Lu.append(i)
        for elem in Lu:
            countL.append(L.count(elem))
        print(dict(zip(Lu,countL)))

    def highest_price(self):
        Mdict={}
        n=int(input("Enter number of items: "))
        for _ in range(n):
            inputS=input("Enter item name and price: ").split(" ")
            key=inputS[0]
            value=float(inputS[1])
            Mdict[key]=value

        max_key=max(Mdict,key=Mdict.get)
        max_value=Mdict[max_key]
        resultD={max_key:max_value}
        print(resultD)

    def num_to_words(self):
        num=[1,2,3,4,5,6,7,8,9]
        num2=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        n=int(input("Enter a number: "))
        i=num.index(n)
        D=dict()
        for x in range(i+1):
            D.update({num[x]:num2[x]})
        print(D)
    
    def sqrt(self,x):
        y=x
        z=(y+(x/y))/2
        while (abs(y-z)>=0.00001):
            y=z
            z=(y+(x/y))/2
        return z

    def string_bin(self):
        string=input("Enter a string: ")
        if string.isdigit():
            return True,string
        else:
            return False,string
    
    def string_bin2(self, string_bin):
        if string_bin[0]:
            if set(string_bin[1])<={'0','1'}:
                    return "Binary string"
            else:
                return "Not Binary string" 


    def test(self):
        s=input("Enter a string: ")
        c=s[len(s)-1]
        r=s[0:len(s)-1]+c.upper()
        print(r)

    def test2(self):
        s=input("Enter a string: ")
        sp="_@$"
        L=0
        U=0
        D=0
        s=0
        for x in s:
            if x.isupper()==True:
                U=U+1
            elif x.islower()==True:
                L=L+1
            elif x.isdigit()==True:
                D=D+1
            elif x in sp:
                s=s+1
            else:
                print("Invalid Password")
        if L<8 or L==0 or U==0 or D==0 or s==0:
            print("Invalid Password")
        else:
            print("Valid Password")


    def test3(self):
        s=input("Enter a string: ")
        L=len(s)//2
        S1=s[0:L]
        S2=s[L:]
        R=S1[-1::-1]+S2[-1::-1]
        R=R[0].upper()+R[1:]
        print(R)

    def test4(self):
        s=input("Enter a string: ")
        testcase=["A","B","C","a","b","c"]
        L=list(s)
        for elem in L:
            if elem in testcase:
                L[L.index(elem)]=str(ord(elem))
        print("".join(L))
        
obj=Unit4()
obj.test4()
