class Student:
    class_year=2024
    num_students=0
    students=[]
    def __init__ (self, name, age):
        self.name=name
        self.age=age
        Student.num_students+=1
        Student.students.append(self)

obj1=Student("Jeetaksh",18)
obj2=Student("Faayim",17)
obj3=Student("Bhoomi",17)

print(f"My class of {Student.class_year} has {Student.num_students} students")

for i,student in enumerate(Student.students):
    print(f"{i+1}. {student.name} is {student.age} years old")

class Animal:
    def __init__(self,name):
        self.name=name
        self.isalive=True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is squeaking")

dog=Dog("Shadow")
cat=Cat("Peanut")
mouse=Mouse("Mickey")

print(dog.name)
print(dog.isalive)
dog.eat()
dog.sleep()
dog.speak()
cat.speak()

class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print("This animal flees")


class Predator(Animal):
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit=Rabbit("Gittu")
hawk=Hawk("Tony")
fish=Fish("Nemo")


rabbit.eat()
hawk.eat()
fish.eat()
fish.sleep()
hawk.sleep()
rabbit.sleep()

from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def go(self):
        pass
    @abstractclassmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("Car is moving")
    def stop(self):
        print("Car is stopped")

class Bicycle(Vehicle):

    def go(self):
        print("Bicycle is moving")
    def stop(self):
        print("Bicycle is stopped")

car=Car()
car.go()
car.stop()
bycycle=Bicycle()
bycycle.go()
bycycle.stop()


class Shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled

class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius=radius

class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.side=width
class Triangle(Shape):
    def __init__(self,color,filled,width,length):
        super().__init__(color,filled)
        self.width=width
        self.length=length

triangle=Triangle("Pink",True,width=10,length=15)
print(triangle.width)
print(triangle.color)
print(triangle.filled)
print(triangle.length)

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Barks")

class Cat(Animal):
    def speak(self):
        print("Meows")

class Car:
    def speak(self):
        print("Honks")


animals = [Dog(), Cat(),Car()]

for animal in animals:
    animal.speak()

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def addBook(self,book):
        self.books.append(book)

    def listBooks(self):
        return [f"{book.title} by {book.author}"for book in self.books]

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

library = Library("Los Angeles Public Library")

book1=Book("The Book","John Doe")
book2=Book("That Book","Jane Doe")  

library.addBook(book1)
library.addBook(book2)

print(library.name)
for book in library.listBooks():
    print(book)

class Engine:
    def __init__ (self,horsepower):
        self.horsepower=horsepower

class Wheel:
    def __init__(self,size):
        self.size=size

class Car:
    def __init__(self,make,model,horsepower,size):
        self.make=make
        self.model=model
        self.engine=Engine(horsepower)
        self.wheels=[Wheel(size)for wheel in range(4)]

    def display(self):
        return f"{self.make} {self.model} {self.engine.horsepower}(hp) {self.wheels[0].size}in"


car = Car("Ford","Mustang",250,20)
car2 = Car("Dodge", "Challenger", 1000, 22)
print(car.display())
print(car2.display())

class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.power=(self.a**self.b) 

    def display(self):  
        print(self.power)
class Circle:
    def __init__ (self,radius):
        self.radius=radius
    def area(self):
        return f"Area of Circle: {(3.14 * self.radius**2):.2f} cm²"
    
    def perimeter(self):
        return f"Perimeter of Circle: {(2 * 3.14 * self.radius):.2f} cm"
    

obj=Circle(5)
print(obj.area())
print(obj.perimeter())


import datetime
class Person:
    def __init__ (self,name,country,DOB):
        self.name=name
        self.country=country
        self.DOB=DOB
        self.Bday=False
    def age(self):
        today=datetime.date.today()
        year=today.year-self.DOB.year

        if (today.month,today.day)<(self.DOB.month,self.DOB.day):
            year-=1
        elif (today.month,today.day)==(self.DOB.month,self.DOB.day):
            self.Bday=True
        return year

    
    def display(self):
        age=self.age()
        if self.Bday:
            print(f"Congratulations {self.name} from {self.country} on your {age}th birthday!")
        else:
            print(f"{self.name} from {self.country} is {self.age()} years old")

person1=Person("Faayim","India",datetime.date(2006,11,24))
person1.display()

