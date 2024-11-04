class Sorting:
    def __init__(self, numbers):
        self.list = numbers  

    def bubble_sort(self):
        for i in range(len(self.list)):
            for j in range(len(self.list)-i-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
        return self.list

    def selection_sort(self):
        for i in range(len(self.list)):
            x = i
            for j in range(i+1, len(self.list)):
                if self.list[j] < self.list[x]:
                    x = j
            self.list[i], self.list[x] = self.list[x], self.list[i]
        return self.list
