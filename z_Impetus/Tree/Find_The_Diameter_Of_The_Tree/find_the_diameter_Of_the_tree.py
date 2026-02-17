class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
from collections import deque

def is_balanced(root):
    
    max_diameter = 0
    
    def height(root):
        nonlocal max_diameter
        if not root:
            return 0
        
        left = height(root.left)
        right = height(root.right)
        
        max_diameter = max(max_diameter, left + right + 1)
        
        return 1 + max(left, right)
    print("max height: ", height(root))
    return max_diameter
            
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
result = is_balanced(root)
print(result)            
