class ClassQ:
    def test1(self):
        n=int(input("Enter a number: "))
        m=n
        sum=0
        while n!=0:
            sum+=(n%10)
            n=n//10
        print(sum)
        if sum<10:
            print(m)
        else:
            print("invalid")
    
    def test2(self):
        Months={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        Days={1:31,2:[28,29],3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        n=int(input("Enter a number: "))
        if n in Months:
            if n!=2:
                print(f"{Months[n]} has {Days[n]} days")
            else:
                print(f"{Months[n]} has {Days[n][0]} and {Days[n][1]} days")
        else:
            print("invalid")
    def test3(self):
        n=int(input("Enter a number: "))
        orgn=n
        L=len(str(n))
        sum=0
        while n!=0:
            x=n%10
            sum+=x**L
            n//=10
        if orgn==sum:
            print(f"{orgn} is an Armstrong number")
        else:
            print(f"{orgn} is not an Armstrong number")

obj=ClassQ()
obj.test3()