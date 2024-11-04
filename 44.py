class Patterns:
    def Rtriangle(self):
        n=int(input("Enter size of pattern: "))
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    
    def Ltriangle(self):
        n=int(input("Enter size of pattern: "))
        for i in range(1,n+1):
            print(" "*(n-i),end=" ")
            for j in range(1,i+1):
                print("*",end="")
            print()
    
    def Ctriangle(self):
        n=int(input("Enter size of pattern: "))
        for i in range(1,n+1):
            print(" "*(n-i),end=" ")
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    
    def UD_Rtriangle(self):
        n=int(input("Enter size of pattern: "))
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()

    def UD_Ltriangle(self):
        n=int(input("Enter size of pattern: "))
        for i in range(n,0,-1):
            print(" "*(n-i),end="")
            for j in range(1,i+1):
                print("*",end="")
            print()
    def UD_Ctriangle(self):
        n=int(input("Enter size of pattern: "))
        for i in range(n,0,-1):
            print(" "*(n-i),end=" ")
            for j in range(1,i+1):
                print("*",end=" ")
            print() 

    def Diamond(self):
        n=int(input("Enter size of pattern: "))
        for i in range(1,n+1):
            print(" "*(n-i),end=" ")
            for j in range(1,i+1):
                print("*",end=" ")
            print()
        for k in range(n-1,0,-1):
            print(" "*(n-k),end=" ")
            for l in range(1,k+1):
                print("*",end=" ")
            print()
    
    def PlusT(self):
        n=int(input("Enter size of pattern: "))
        for i in range(1,n+1):
            if i!=5:
                for j in range(1,i+1):
                    print("*",end=" ")
                print()
            elif i==5:
                for j in range(1,i+1):
                    print("+",end=" ")
                print()

    def LeftTriangle(self):
        n=int(input("Enter size of pattern: "))
        for i in range(1,n+1):  
            for j in range(n,0,-1):  
                if j > i:
                    print(" ", end=" ") 
                else:
                    print(i, end=" ") 
            print()


    def LeftT(self):
        n=int(input("Enter size of pattern: "))
        for i in range(1,n+1):
            for j in range(n,0,-1):
                if j>i:
                    print(" ",end=" ")
                else:
                    print("*",end=" ")
            print()
def main():
    obj=Patterns()
    obj.Rtriangle()
    obj.Ltriangle()
    obj.Ctriangle()
    obj.UD_Rtriangle()
    obj.UD_Ltriangle()
    obj.UD_Ctriangle()
    obj.Diamond()
    obj.PlusT()
    obj.LeftTriangle()
    obj.LeftT()

if __name__ == "__main__":
    main()
