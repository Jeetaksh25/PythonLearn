def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def combination(n,r):
    comb=factorial(n)/(factorial(r)*factorial(n-r))
    return comb

def permutation(n,r):
    perm = combination(n,r)*factorial(r)
    return perm
c1=int(input("Enter 1 for combination and 2 for permutation: "))
if c1==1:
    n=int(input("Enter the value of n: "))
    r=int(input("Enter the value of r: "))
    print(combination(n,r))
elif c1==2:
    n=int(input("Enter the value of n: "))
    r=int(input("Enter the value of r: "))
    print(permutation(n,r))