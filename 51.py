import math

class Trigonometry:
    def Factorial(self, x):
        if x==0 or x==1:
            return 1
        return x*self.Factorial(x-1)
    
    def DegreeToRad(self,x):
        return x*(math.pi/180)
    
    def Sin(self,x):
        if x==90:
            return 1.0  
        x=self.DegreeToRad(x)
        result=x
        for i in range(3,100,2): 
            sign=(-1)**((i-1)//2)
            result+=sign*(x**i/self.Factorial(i))
        return round(result,4)

    def Cos(self,x):
        if x==90:
            return 0.0  
        x=self.DegreeToRad(x)
        result=1
        for i in range(2,100,2):  
            sign=(-1)**(i//2)
            result+=sign*(x**i/self.Factorial(i))
        return round(result,4)
    
    def Tan(self,x):
        cosx=self.Cos(x)
        if cosx==0:
            return float('inf')  
        return round(self.Sin(x)/cosx,4)

    def Cosec(self,x):
        sinx=self.Sin(x)
        if sinx==0:
            return float('inf') 
        return round(1/sinx,4)

    def Sec(self,x):
        cosx=self.Cos(x)
        if cosx==0:
            return float('inf') 
        return round(1/cosx,4)
    
    def Cot(self,x):
        tanx=self.Tan(x)
        if tanx==0:
            return float('inf') 
        return round(1/tanx,4)

    def Cosh(self,x):
        result=1
        for i in range(2,100,2):
            result+=(x**i)/self.Factorial(i)
        return round(result,4)

    def Sinh(self,x):
        result=x
        for i in range(3,100,2):
            result+=(x**i)/self.Factorial(i)
        return round(result,4)
    
    def ex(self,x):
        return round(self.Cosh(x)+self.Sinh(x),4)

obj = Trigonometry()
x = int(input("Enter the angle: "))
print(f"Sin({x}) = {obj.Sin(x)}")
print(f"Cos({x}) = {obj.Cos(x)}")
print(f"Tan({x}) = {obj.Tan(x)}")
print(f"Cosec({x}) = {obj.Cosec(x)}")
print(f"Sec({x}) = {obj.Sec(x)}")
print(f"Cot({x}) = {obj.Cot(x)}")
print(f"ex({x}) = {obj.ex(x)}")
print(f"Sinh({x}) = {obj.Sinh(x)}")
print(f"Cosh({x}) = {obj.Cosh(x)}")
