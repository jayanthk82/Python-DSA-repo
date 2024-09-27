class HEAP:
    def __init__(self) -> None:
        self.minheap = list()
    def insert(self,element):
        self.minheap.append(element)
        self.heap_up(len(self.minheap)-1)
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
    def heap_up(self,index):
        if index==0:
            return
        parent = int((index-1)/2)
        if self.minheap[index] < self.minheap[parent]:
            self.minheap[parent],self.minheap[index] = self.minheap[index],self.minheap[parent]
            self.heap_up(parent)
    def display(self):
        print(self.minheap)
object = HEAP()

object.insert(5)
object.insert(7)
object.insert(9)
object.insert(0)
object.insert(1)
object.insert(5)
object.insert(12)
object.insert(11)

object.delete()
object.delete()
object.delete()
object.delete()
object.delete()
object.delete()
object.delete()
object.delete()
object.display()





