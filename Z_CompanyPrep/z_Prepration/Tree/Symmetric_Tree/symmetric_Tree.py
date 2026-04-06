class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def is_symmetric(root):
    
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        
        if not t1 or not t2:
            return False
        
        return (t1.value == t2.value and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))
    
    if not root:
        return True
    
    return is_mirror(root.left, root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(is_symmetric(root))  # True
