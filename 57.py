class number:
    def perfectNotillK(self):
        sum=0
        for i in range(1,1000):
            for j in range(1,i):
                if i%j==0:
                    sum+=j
            if sum==i:
                print(i)
            sum=0

def main():
    obj=number()
    obj.perfectNotillK()

if __name__=="__main__":
    main()