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
        
mycar = Unit5.Honda()
mycar.setEngineModel("4.5L V8")
mycar.setCarModel("NSX")
mycar.getEngineModel()
mycar.getCarModel()