import random
class quicksort:

    def __init__(self,list):
        self.list = list
        length = len(list)
        self.list = self.sort(list,0,length)
        print(self.list)

    def sort(self,list,low,high):
        if low>=high:
            return list
        
        if low!=high:
            self.pivot_index = random.randint(low,high-1)
            self.pivot = list[self.pivot_index]

        start = low
        end=high-1

        while(start<end):
            while(list[start]<self.pivot):
                start+=1
            while(list[end]>self.pivot):
                end-=1
            if start<end:
                list[start],list[end] = list[end],list[start]  

        self.pivot_index = end
        list = self.sort(list,low,self.pivot_index)          
        list = self.sort(list,self.pivot_index+1,high)
        return list
list = [1,7,6,4,8,0,2]
object = quicksort(list)
