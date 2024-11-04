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

num=int(input("Enter number of rectangles: "))

for i in range(num):
    x=float(input("Enter Length: "))
    y=float(input("Enter Breadth: "))
    z=input("Enter units: ")
    obj=Unit5.rectangle(x,y,z)
    obj.AreaOfRectangle()
            