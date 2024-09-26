class min_heap:

    def __init__(self,list1=None):
        self.heap = list()
        self.list1 = list1

    def heapify_up(self,index):
        if index==0:
            return
        parent_index = int((index-1)/2)
        if self.heap[parent_index]>self.heap[index]:
            self.heap[parent_index],self.heap[index] = self.heap[index],self.heap[parent_index]
            self.heapify_up(parent_index) 

    def insert(self,element):
        self.heap.append(element)
        self.heapify_up(len(self.heap)-1)

    def heapify_down(self,index):
        left_child = 2*index+1
        right_child = 2*index+2
        smallest = index
        if left_child < len(self.heap) and self.heap[left_child]<self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child]<self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index],self.heap[smallest] = self.heap[smallest],self.heap[index]
            self.heapify_down(smallest)

    def down_top_heap(self):
        for i in range(0, (len(self.heap) - 1) // 2):
            self.build_heap(i)
            
    def build_heap(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]

    def display(self):
        print(self.heap)

heap_topdown = min_heap()
list1 = [1,2,3,4,5,6]
heap_build = min_heap(list1)

     

