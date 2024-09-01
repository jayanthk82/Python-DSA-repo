# CIRCULAR QUEUE 
class queuel:
    def __init__(self,size):
        self.n= size
        self.queue = [None]*size
        self.front,self.rear = None,None

    # METHOD TO INSERT ELEMENT IN QUEUE
    def enqueue(self,element):
        if(self.rear==None and self.front==None):
            self.rear=0
            self.front=0
        elif(self.rear==None):
            self.rear = 0
            
        else:
            self.rear = self.rear+1
        if(self.rear<self.n and self.queue[self.rear]==None):
            self.queue[self.rear] = element
            print('element inserted')
            return
        elif(self.rear==self.n):
            self.rear = None
            self.enqueue(element)
        else:
            self.rear = self.n - 1
            print('queue is full')


    # METHOD TO REMOVE AND RETURN THE FRONT ELEMENT
    def dequeue(self):
        if(self.front==None and self.queue[0]!=None ):
            self.front=0
            print(self.queue[self.front])
            self.queue[self.front] = None
        elif(self.front==None):
            print("Queue is empty")
        else:
            a = self.queue[self.front]
            self.queue[self.front] = None
            self.front=self.front+1
            print(a)
        
        if(self.front != None and self.queue[self.front + 1] == None):
            self.front = None
            self.rear = None
        elif(self.front!=None and self.queue[self.front+1]!=None): 
            self.front = self.front+1

    # METHOD TO DISPLAY THE QUEUE
    def display(self):
        print(self.queue)
        print('\nfront = ',self.front)
        print('\nrear = ',self.rear)
