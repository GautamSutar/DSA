class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=" ")
            self.inorder_traversal(root.right)
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.inorder_traversal(root)
