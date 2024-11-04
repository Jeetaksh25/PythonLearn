class BubbleSort:
    def __init__ (self, *args):
        self.list = list(args)
        self.BubbleSort = self.bubble_sort()
    def bubble_sort(self):
        for i in range(len(self.list)-1):
            for j in range(len(self.list)-i-1):
                if self.list[j] > self.list[j+1]:
                    temp = self.list[j]
                    self.list[j] = self.list[j+1]
                    self.list[j+1] = temp
        return self.list
    
elemS = int(input("Enter number of elements: "))
List = []
for i in range(elemS):
    List.append(int(input(f"Enter element #{i+1}: ")))
obj = BubbleSort(*List)
print(f"Your sorted list is: {obj.BubbleSort}")