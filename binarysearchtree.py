class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self, numbers):
        self.root = None
        self.numbers = list(map(int, numbers))

    def insert(self):
        for i in self.numbers:
            if self.root is None:
                self.root = node(i)
            else:
                self._insert(self.root, i)
        return self.root

    def _insert(self, root, data):
        if root is None:
            root = node(data)
            return root
        if data > root.data:
            root.right = self._insert(root.right, data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        return root

    def deletion(self, root, value):
        position_temp = root
        if root is None:
            return root  

        predecessor = None
        successor = None
        pre_position = None

        while position_temp and position_temp.data != value:
            pre_position = position_temp
            if value > position_temp.data:
                position_temp = position_temp.right
            else:
                position_temp = position_temp.left

        if position_temp is None:
            return root

        if position_temp.left is None and position_temp.right is None:
            if pre_position.left == position_temp:
                pre_position.left = None
            else:
                pre_position.right = None
            return root
        if position_temp.left is not None:
            predecessor = position_temp.left
            while predecessor.right is not None:
                predecessor = predecessor.right
            position_temp.data = predecessor.data 
            position_temp.left = self.deletion(position_temp.left, predecessor.data)  

        elif position_temp.right is not None:
            successor = position_temp.right
            while successor.left is not None:
                successor = successor.left
            position_temp.data = successor.data  
            position_temp.right = self.deletion(position_temp.right, successor.data)  

        return root

    def display(self, root):
        if root is not None:
            self.display(root.left)
            print(root.data)
            self.display(root.right)

object = BST('8374753179')
root = object.insert()
object.display(root)
object.deletion(root, 9)
print('\n')
object.display(root)
