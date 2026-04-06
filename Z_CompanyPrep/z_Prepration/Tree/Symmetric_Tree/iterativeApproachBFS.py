class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def is_symmetric(root):
    if not root:
        return True
    queue = deque([(root.left, root.right)])
    while queue:
        t1, t2 = queue.popleft()
        
        if not t1 and not t2:
            continue
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        queue.append((t1.left, t2.right))
        queue.append((t1.right, t2.left))
    return True
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(is_symmetric(root))  
