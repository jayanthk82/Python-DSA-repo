class queue:
    def __init__(self,size):
        self.size = size
        self.s1 = [None]*self.size
        self.s2 = [None]*self.size
        self.t1,self.t2 = -1,-1
    def enqueue(self,element):
        if(self.t1==self.size-1):
            if(self.t2>-1):
                print("Queue is full")
                return 
            else:
                while(self.t1>-1):
                    self.t2 = self.t2+1
                    self.s2[self.t2] = self.s1[self.t1]
                    self.t1=self.t1 -1
                self.t1 = self.t1+1
                self.s1[self.t1] = element
                print("element inserted")
                return
        else:
            self.t1 = self.t1+1
            self.s1[self.t1] = element
            print("element inserted")
            return
    def dequeue(self):
        if(self.t2>-1):
            print(self.s2[self.t2])
            self.t2 = self.t2-1
            return
        elif(self.t1>-1):
            while(self.t1>-1):
                self.t2 = self.t2+1
                self.s2[self.t2] = self.s1[self.t1]
                self.t1=self.t1 -1      
            self.dequeue()     




    
