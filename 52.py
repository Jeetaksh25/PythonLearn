class StringF:
    def reverse_string(self, string):
        sL=[]
        for elem in string:
            sL.append(elem)
        sL.reverse()
        return "".join(sL)

    def reverse_words(self,string):
        result=str("")
        idx=0
        for elem in string:
            if ord(elem)==32:
                idx=string.index(elem)
        for i in range(idx+1,len(string)):
            result=result+string[i]
        result=result+" "
        for i in range(0,idx+1):
            result=result+string[i]
        return result

    def swap_FnL(self,num):
        num=str(num)
        Fnum=num[0]
        Lnum=num[-1]
        num=num[1:-1]
        num=Lnum+num+Fnum
        num=int(num)
        return num   

obj=StringF()
print(obj.swap_FnL(input("Enter a number: ")))
