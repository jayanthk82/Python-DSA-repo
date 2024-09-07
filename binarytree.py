class node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None


class binary_tree:
    def TREE(self):
        data = int(input('data'))
        root = node(data)
        L = int(input('1 TO LEFT'))
        if(L==1):  
            root.left=self.TREE()
        R = int(input('1 TO RIGHT'))
        if(R==1):    
            root.right = self.TREE()
        return root
    def display(self,root):
        if(root!=None):
            self.display(root.left)
            print(root.data)
            self.display(root.right)
        
object = binary_tree()
root = object.TREE()
object.display(root)
















































































































'''class binary_tree:
    def __init__(self, infix, postfix):
        self.infix = infix
        self.postfix = postfix

    def tree(self):
        # Create a dictionary to store the index of each element in the infix expression
        index_map = {char: i for i, char in enumerate(self.infix)}

        # Define a recursive function to construct the binary tree
        def construct_tree(postfix, start, end):
            if start > end:
                return None

            # Get the current node's value from the postfix expression
            node_value = postfix.pop()

            # Create a new node
            current_node = node(node_value)

            # If the node is an operator, recursively construct its left and right subtrees
            if node_value in '+-*/':
                # Get the index of the current node in the infix expression
                index = index_map[node_value]

                # Recursively construct the right subtree
                current_node.right = construct_tree(postfix, index + 1, end)

                # Recursively construct the left subtree
                current_node.left = construct_tree(postfix, start, index - 1)

            return current_node

        # Convert the postfix expression to a list for easier manipulation
        postfix_list = list(self.postfix)

        # Construct the binary tree
        root = construct_tree(postfix_list, 0, len(self.infix) - 1)

        return root

    def print_tree(self, root, level=0):
        if root is not None:
            self.print_tree(root.right, level + 1)
            print(' ' * 4 * level + '->', root.data)
            self.print_tree(root.left, level + 1)


# Example usage:
infix = "A+B*C"
postfix = "ABC*+"
tree = binary_tree(infix, postfix)
root = tree.tree()
tree.print_tree(root)
'''