class Maping:
    def uniquelist(self):
        elem=list(map(str, filter(None, input("Enter elements: ").split(" "))))
        elem2=[]
        for elem1 in elem:
            if elem1 not in elem2:
                elem2.append(elem1)
        for i in elem2:
            x=str(i)
            print(x,end=" ")
        
    def uniquestring(self):
        S=input("Enter string: ")
        L=list(S)
        L2=[]
        for i in L:
            if i not in L2:
                L2.append(i)
        for i in L2:
            print(i,end=" ")

func=Maping()
func.uniquestring()
