
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque

def left_view(root):
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
    
    print(result)
        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.right.right = Node(6)
left_view(root)
