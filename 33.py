class Maths:
    def __init__ (self,n):
        self.n=n
        self.checkdiv3_5 = self.check_div_3_5()
    def check_div_3_5(self):
        if self.n%3==0 and self.n%5==0:
            return True
        else:
            return False
    
num=int(input("Enter a number: "))
func=Maths(num)
if func.checkdiv3_5:
    print(f"{num} is a multiple of 3 and 5")
else:
    print(f"{num} is not a multiple of 3 and 5")