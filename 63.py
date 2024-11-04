class Solution(object):
    def reverseString(self, s):
        L=list(s)
        L2=[]
        for i in range(len(L),0,-1):
            L2.append(L[i-1])
        return L2

obj=Solution()
print(obj.reverseString(input("Enter a string: ")))