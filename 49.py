def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(int(input("Enter a number: "))))

def Sum(n):
    if n == 0:
        return 0
    else:
        return n+Sum(n-1)

print(Sum(int(input("Enter a number: "))))