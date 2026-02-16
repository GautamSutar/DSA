class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
from collections import deque
def top_view(root):
    
    hd_map = {}
    queue = deque([(root, 0)])
    if not root:
        return 
    
    while queue:
        node, hd = queue.popleft()
        
        if hd not in hd_map:
            hd_map[hd] = node.val
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
            
    return [hd_map[key] for key in sorted(hd_map)]
            
            
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(6)
root.right.right = Node(5)
result = top_view(root)
print(result)            
            
            
            
            
            
            
            
            
            
            
            