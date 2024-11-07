class Unit5:
    class student:
        def __init__(self,name,reg,rno):
            self.name=name
            self.reg=reg
            self.rno=rno
        def put(self):
            print(f"Name: {self.name}")
            print(f"RegNo: {self.reg}")
            print(f"RollNo: {self.rno}")

    class rectangle:
        def __init__(self,length,breadth,unit):
            self.length=length
            self.breadth=breadth
            self.unit=unit
        
        def AreaOfRectangle(self):
            print(f"Area of Rectangle: {self.length * self.breadth} {self.unit}^2")

    class Test:
        def __init__(self,a,b):
            self.a=a
            self.b=b
            self.power=(self.a**self.b)
        def put(self):
            print(f"Power: {self.power}")


    class Company:
        def __init__ (self,name,cc,price):
            self.name=name
            self.cc=cc
            self.price=price
        def displayCompanywithhighestcc(self):
            print(f"Name: {self.name}")
            print(f"CC: {self.cc}")
            print(f"Price: {self.price}")

    class Employee:
        def __init__ (self,name,salary):
            self.name=name
            self.salary=salary
        def display(self):
            print(f"Name: {self.name}")
            print(f"Salary: ${self.salary}")

    class Volume:
        def __init__ (self,radius,height):
            self.radius=radius
            self.height=height

        def volumeCylinder(self):
            print(f"Volume of Cylinder: {3.14 * self.radius * self.radius * self.height}")
        
        def volumeSphere(self):
            print(f"Volume of Sphere: {(4/3) * 3.14 * self.radius * self.radius * self.radius}")

        def volumeCone(self):
            print(f"Volume of Cone: {(1/3) * 3.14 * self.radius * self.radius * self.height}")

    class ParentClass:
        def __init__ (self,name,age):
            self.name=name
            self.age=age
        def display(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")

    class ChildClass(ParentClass):
        def __init__ (self,name,age,rollno):
            super().__init__(name,age)
            self.rollno=rollno
        def display(self):
            super().display()
            print(f"RollNo: {self.rollno}")

    class volume_parent:
        def __init__ (self,radius):
            self.radius=radius
    class volume_child(volume_parent):
        def volumeSphere(self):
            print(f"Volume of Sphere: {(4/3) * 3.14 * self.radius * self.radius * self.radius}")


    class A:
        def get_a(self):
            self.a=int(input("Enter a: "))

    class B(A):
        def get_b(self):
            self.b=int(input("Enter b: "))
        
    class C(B):
        def get_c(self):
            self.c=int(input("Enter c: "))
    
        def put(self):
            print(f"a: {self.a}")
            print(f"b: {self.b}")
            print(f"c: {self.c}")

               
    class Car:
        def setEngineModel(self,engine):
            self.engine=engine
        def getEngineModel(self):
            print(f"Engine Model: {self.engine}")
        
    class Honda(Car):
        def setCarModel(self,model):
            self.model=model
        def getCarModel(self):
            print(f"Car Model: {self.model}")

    class P:
        def getEven(self,L):
            self.L=L
            self.E=[]
            for x in self.L:
                if int(x)%2==0:
                    self.E.append(x)
            return self.E
    
    class C(P):
        def getOdd(self):
            self.O=[]
            for x in self.L:
                if int(x)%2!=0:
                    self.O.append(x)
            return self.O
    
    class G(C):
        def getSorted(self):
            self.L.sort()
            return self.L
        
    class Polygon:
        def __init__(self):
            self.sideNo=0
            self.choice=0
        
        def getChoice(self):
            print("1. Rectangle\n2. Pentagon")
            self.choice=int(input("Enter your choice: "))
            if self.choice==1:
                self.sideNo=4
                return Unit5.Rectangle()  
            elif self.choice==2:
                self.sideNo=5
                return Unit5.Penagon()
            else:
                print("Invalid choice")
                return None

    class Rectangle(Polygon):
        def __init__(self):
            super().__init__()
            self.sideNo=4
            self.sides=[]
        def inputSides(self):
            for i in range(self.sideNo):
                x=int(input(f"Enter side {i+1}: "))
                self.sides.append(x)
        
        def displaySides(self):
            for i in range(self.sideNo):
                print(f"Side {i+1}: {self.sides[i]}")
    
    class Penagon(Polygon):
        def __init__(self):
            super().__init__()
            self.sideNo=5
            self.sides=[]
        def inputSides(self):
            for i in range(self.sideNo):
                x=int(input(f"Enter side {i+1}: "))
                self.sides.append(x)
        
        def displaySides(self):
            for i in range(self.sideNo):
                print(f"Side {i+1}: {self.sides[i]}")

"""class Vehicle:
    def __init__(self, name, price, regno):
        self.name = name
        self.price = price
        self.regno = regno

class Car(Vehicle):
    def __init__(self, name, price, regno, gear):
        super().__init__(name, price, regno)
        self.gear = gear

class Boat(Vehicle):
    def __init__(self, name, price, regno, capacity):
        super().__init__(name, price, regno)
        self.capacity = capacity

class Hover(Car, Boat):
    def __init__(self, name, price, regno, gear, capacity):
        Car.__init__(self, name, price, regno, gear)
        Boat.__init__(self, name, price, regno, capacity)

obj = Car("Ferrari", 3500000, "AP 12 3456", 9)
obj2 = Boat("Lamborghini", 550000, "HR 12 U 7965", 12)
obj3 = Hover("Mercedes", 250000, "BATMAN77", 8, 12)
print(obj3.name, obj3.price, obj3.regno, obj3.gear, obj3.capacity)"""


obj=Unit5.Polygon()
choice1=obj.getChoice()
if choice1:
    choice1.inputSides()
    choice1.displaySides()