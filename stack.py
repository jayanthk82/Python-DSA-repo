#IMPLEMENTATION USING ARRAY

class stack:
    
    stack = list()
    top = -1
    def push(self,item):    
        self.top=self.top+1
        self.stack.append(item)
        print('item inserted at the top')
    def pop(self):
        if(self.top==-1):
            print("stack is empty")
        else:
            print(self.stack[self.top],'\n')
            self.top=self.top-1
    def display(self):
        while(self.top!=-1):
            self.pop()


#IMPLEMENTATION USING LINKEDLIST
class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class stack:
    head = None
    def push(self,data):
        newnode = node()
        newnode.data = data
        if(self.head==None):
            self.head = newnode
        else:
             newnode.next = self.head
             self.head = newnode
    def pop(self):
        if(self.head==None):
            print('stack is empty')
        else:
            print(self.head.data,'\n')
            self.head = self.head.next
    def display(self):
        if(self.head==None):
            print('stack is empty')
        while(self.head!=None):
            self.pop()


