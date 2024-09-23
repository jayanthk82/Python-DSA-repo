class selectionsort:
    def __init__(self,list):
        self.list = list
        self.selection_sort()
        self.display()
    def selection_sort(self):
        self.swap_index = None
        for i in range(0,len(self.list)):
            self.swap_index=i
            for j in range(i,len(self.list)):
                if self.list[self.swap_index]>self.list[j]:
                    self.swap_index = j
            self.list[i],self.list[self.swap_index]=self.list[self.swap_index],self.list[i]    
    def display(self):
        print(self.list)
list = [1,7,6,4,8,1,2]
object = selectionsort(list)