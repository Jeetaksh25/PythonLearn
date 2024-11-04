MonthlySalary=float(input("Enter the monthly salary: "))
GrossSalary=MonthlySalary*12
if GrossSalary<250000:
    Tax=0
elif 250000<=GrossSalary<500000:
    Tax=(GrossSalary-250000)*0.05
elif 500000<=GrossSalary<750000:
    Tax=(GrossSalary-500000)*0.1
elif 750000<=GrossSalary<1000000:
    Tax=(GrossSalary-750000)*0.15
else:
    Tax=(GrossSalary-1000000)*0.2
NetSalary=GrossSalary-Tax
print("The monthly salary is: ",MonthlySalary)
print("The gross salary is: ",GrossSalary)
print("The tax is: ",Tax)
print("The net salary is: ",NetSalary)
