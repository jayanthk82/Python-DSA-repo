class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self,numbers):
        self.root = None
        self.numbers = list(map(int,numbers))
    def insert(self):
        for i in self.numbers:
            if self.root is None:
                self.root = node(i)
            else:
                self._insert(self.root,i)
        return self.root

    def _insert(self,root,data):
        if root==None:
            iroot = node(data)
            return iroot
        if data>root.data:
            root.right = self._insert(root.right,data)
        if data<root.data:
            root.left = self._insert(root.left,data)
        return root
    

    def display(self,root):
        if root!= None:
            self.display(root.left)
            print(root.data)
            self.display(root.right)
object = BST('8374753179')
root=object.insert()
object.display(root)

        
        


            


                
