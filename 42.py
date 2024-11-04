class Primefromlist:
    def __init__(self, n):
        self.n = n
        self.L2 = self.lfunc() 
        self.check_prime()  
    
    def lfunc(self):
        S = input("Enter the string: ")
        S = S.replace(",", "")  
        L = list(S)  
        L2 = []
        for x in L:
            if x.isdigit() and x not in L2:
                L2.append(x)
        
        return L2  
    
    def check_prime(self):
        for num_str in self.L2:
            num = int(num_str)  
            if self.is_prime(num):
                print(f"{num} is a prime number")
            else:
                print(f"{num} is not a prime number")
    
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

obj = Primefromlist(0)
