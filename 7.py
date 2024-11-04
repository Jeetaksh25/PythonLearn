x3=float(input("Enter the coefficient of x^3: "))
x2=float(input("Enter the coefficient of x^2: "))
x1=float(input("Enter the coefficient of x: "))
x0=float(input("Enter the constant term: "))


def hitntrial(x3,x2,x1,x0):
    for i in range(-999,999):
        t=i
        if x3*t**3 + x2*t**2 + x1*t + x0 == 0:
            return t
        
print("The equation is: ",x3,"x^3 + ",x2,"x^2 + ",x1,"x + ",x0," = 0")
root1=hitntrial(x3,x2,x1,x0)
print("The roots are: ",root1)



      