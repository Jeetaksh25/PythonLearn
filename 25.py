import time
while 1==1:    
    for i in range(1,31):
        for j in range(1,i+1):
            print(j,end=" ")
            time.sleep(0.001)
        print()
        del j
    del i
    for i in range(29,1,-1):
        for j in range(1,i+1):
            print(j,end=" ")
            time.sleep(0.001)
        print()
        del j
    del i