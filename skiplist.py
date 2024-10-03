class node:
    def __init__(self,data) -> None:
        self.data = data
        self.levels = [None]*5
    
class skiplist:
    def __init__(self):
        self.head = [None]*5
        self.current_level = 0
    def insert(self,data):
        newnode = node(data)
        if self.head[0]==None:
            self.head[0] = newnode
            return
        temp_head = self.head[0]
        while temp_head.self.levels[0] != None:
            if temp_head.self.data < data:
                temp_head = temp_head.self.levels[0]
            else:
                break
        newnode.levels[0] = temp_head.levels[0] 


                         
        