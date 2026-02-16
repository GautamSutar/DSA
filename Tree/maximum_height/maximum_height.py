class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
from collections import deque

def is_balanced(root):
    def check_height(root):
        if not root:
            return 0
            
        left_height = check_height(root.left)
        right_height = check_height(root.right)
        
        return 1 + max(left_height, right_height)
    
    return check_height(root)
            
            
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
result = is_balanced(root)
print(result)            
