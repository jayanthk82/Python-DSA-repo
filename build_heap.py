class HEAP:
    def insert(self,list):
        self.minheap = list
        mid = int(len(self.minheap)-1)//2
        while(mid>=0):
            self.build_heap(mid)    
            mid-=1
    def delete(self):
        print(self.minheap[0])
        if len(self.minheap)==1:
            self.minheap.pop()
            return
        last=self.minheap.pop()
        self.minheap[0] = last
        self.extract_min(0)
    def extract_min(self,parent):
        if parent>=len(self.minheap):
            return
        index = parent
        leftchild = 2*index+1
        rightchild = leftchild+1
        minimum = self.minheap[index]
        if leftchild<len(self.minheap) and minimum > self.minheap[leftchild]:
            minimum=self.minheap[leftchild]
            index = leftchild
        if rightchild<len(self.minheap)  and minimum>self.minheap[rightchild]:
            minimum = self.minheap[rightchild]
            index = rightchild
        if index != parent:
            self.minheap[parent],self.minheap[index] = self.minheap[index],self.minheap[parent]
            self.extract_min(index)
    def build_heap(self,parent): 
        index = parent
        leftchild = 2*index+1
        rightchild = leftchild+1
        minimum = self.minheap[index]
        if leftchild<len(self.minheap) and minimum > self.minheap[leftchild]:
            minimum=self.minheap[leftchild]
            index = leftchild
        if rightchild<len(self.minheap)  and minimum>self.minheap[rightchild]:
            minimum = self.minheap[rightchild]
            index = rightchild
        if index != parent:
            self.minheap[parent],self.minheap[index] = self.minheap[index],self.minheap[parent]
    def display(self):
        print(self.minheap)
        
list = [5,7,9,0,1,5,12,11]
object = HEAP()
object.insert(list)
object.delete()
object.display()