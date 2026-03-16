class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
from collections import deque

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))
def is_balanced(root):
    if not root:
        return True

    left_height = height(root.left)
    right_height = height(root.right)
            
    if abs(left_height - right_height) > 1:
        return False
        
    return is_balanced(root.left) and is_balanced(root.right)
            
            
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.left.left = Node(3)
result1 = is_balanced(root)
result2 = is_balanced(root2)
print(result1)            
print(result2) 
            