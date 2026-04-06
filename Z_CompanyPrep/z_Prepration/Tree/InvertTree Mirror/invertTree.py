class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left 
    invert_tree(root.left)
    invert_tree(root.right)
    return root



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)


result = invert_tree(root)
print(result.left.left.val)
