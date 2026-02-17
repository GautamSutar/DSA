class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
from collections import deque

def is_balanced(root):
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1 
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth
            
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
result = is_balanced(root)
print(result)            

            
            
            
            
            
            
            
            
            
            