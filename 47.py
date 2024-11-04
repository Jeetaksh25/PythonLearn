class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return bool(0)
        string=str(x)
        length=len(string)
        first_part=str()
        second_part=str()
        if length%2==0:
            first_part=string[0:int(length/2)]
            second_part=string[length:int(length/2)-1:-1]
        elif length%2!=0:
            first_part=string[0:int(length//2)]
            second_part=string[length:int(length//2):-1]

        if first_part==second_part:
            return bool(1)
        else:
            return bool(0)
while 1==1:
    n=int(input("Enter an integer: "))
    obj=Solution()
    print(obj.isPalindrome(n))
