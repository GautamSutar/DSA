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
        if left_height == -1:
            return -1 
        
        right_height = check_height(root.right)
        if right_height == -1:
            return -1 
            
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return check_height(root) != -1
            
            
            
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
                       