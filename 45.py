class Solution(object):
    def reverse1(self, x):
        self.pop=[]
        while x!=0:
            self.pop.append(x%10)
            x=x//10
        x=str(self.pop[0])
        for i in range(1,len(self.pop)):
            x=str(x)+str(self.pop[i])
        return int(x)

    def reverse(self, x):
        rev=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x!=0:
            pop=x%10
            x=x//10
            if ((pop>(2**31-1)//10) or (pop==(2**31-1)//10 and pop>7)):
                return 0 
            rev=rev*10+pop
        return sign*rev
    
    def reverse2(self, x):
        rev=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x!=0:
            pop=x%10
            x//=10
            if rev>(2**31-1)//10 or (rev==(2**31-1)//10 and pop>7):
                return 0
            rev=rev*10+pop
        return sign*rev
    
    def findMedianSortedArrays(self, nums1, nums2):
        x=nums1.sort()
        y=nums2.sort()
        z=x+y
        return z       
    
n=list(map(int,input().split(" ")))
m=list(map(int,input().split(" ")))
obj=Solution()
print(obj.findMedianSortedArrays(n,m))
