class Solution(object):
    def isHappy(self, n):
        def sum(n):
            sum=0
            while n>0:
                digit=n%10
                n=n//10
                sum=sum+digit**2
            return sum
        Happy=set()
        while n!=1 and n not in Happy:
            Happy.add(n)
            n=sum(n)
        return n==1
        
obj=Solution()
print(obj.isHappy(19))