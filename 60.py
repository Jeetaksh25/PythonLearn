class Solution(object):
    def sqrt(self,n):
        if 0<=n and n<2:
            return n
        y=n
        z=(y+(n/y))/2
        while(abs(y-z)>=0.00001):
            y=z
            z=(y+(n/y))/2
        return z
    def checkPerfectNumber(self, num):
        if num==1:
            return False
        sum=1
        for i in range(2,int(self.sqrt(num))+1):
            if num%i==0:
                sum+=i
                sum+=num/i
        return sum==num

obj=Solution()
print(obj.checkPerfectNumber(6))