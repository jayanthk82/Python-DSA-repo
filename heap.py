class min_heap:
    def __init__(self):
        self.heap = list()
    def heapify_up(self,index):
        if index==0:
            return
        parent_index = int((index-1)/2)
        if self.heap[parent_index]>self.heap[index]:
            self.heap[parent_index],self.heap[index] = self.heap[index],self.heap[parent_index]
            self.heapify_up(parent_index)
    def heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def insert(self,key):    
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)


    def display(self):
        print(self.heap)
    
    def extract_min(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_element
        

object = min_heap()
object.insert(10)
object.insert(19)
object.insert(1)
object.insert(11)
object.insert(55)
object.display() 
min = object.extract_min()
print(min)


     

