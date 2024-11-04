class Solution(object):
    def myAtoi(self, s):
        s=s.strip()
        x=0
        if not s:
            return 0
        if not ((48 <= ord(s[0]) <= 57) or s[0] == "+" or s[0] == "-"):
            return 0
        if s[0]=="-":
            for i in range(1,len(s)):
                if s[i]==".":
                    break
                if not (48 <= ord(s[i]) <= 57):
                    break
                else:
                    x=-abs(int(s[:i+1]))
        elif s[0]=="+":
            for i in range(1,len(s)):
                if s[i]==".":
                      break
                if not (48 <= ord(s[i]) <= 57):
                    break
                else:
                    x=int(s[:i+1])

        elif (48<=ord(s[0])<=57):
            for i in range(0,len(s)):
                if s[i]==".":
                    break
                if not (48 <= ord(s[i]) <= 57):
                    break
                else:
                    x=int(s[:i+1])

        if x > 2**31 - 1:
            return 2**31 - 1
        elif x < -2**31:
            return -2**31
        return x

obj=Solution()
print(obj.myAtoi(input("Enter a string: ")))