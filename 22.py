def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def is_armstrong(n):
    total = 0
    x = str(n)  
    for digit in x:
        total += factorial(int(digit))  
    return total == n

ch1=int(input("Enter 1 to input a number to check for armstrong number or 2 for all armstrong numbers from 1 to 100000: "))
if ch1==1:
    n=int(input("Enter the number: "))
    if is_armstrong(n):
        print(n, "is an Armstrong number.")
    else:
        print(n, "is not an Armstrong number.")
elif ch1==2:
    print("All Armstrong numbers from 1 to 100000 are: ")
    for i in range(1, 100001):
        if is_armstrong(i):
            print(i)
