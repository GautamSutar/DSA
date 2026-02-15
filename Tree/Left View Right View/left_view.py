class Node:
    def __init_(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque

def left_view(root):
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
left_view(root)
