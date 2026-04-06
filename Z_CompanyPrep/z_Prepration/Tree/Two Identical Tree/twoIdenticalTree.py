class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    
def idetincal_tree(root, root2):
    if not root and not root2:
        return True
    if not root or not root2:
        return None
    return (root.val == root2.val and idetincal_tree(root.left, root2.left) and idetincal_tree(root.right, root2.right))



root = Node(1)
root.left = Node(2)
root.right = Node(3)

# Tree 2
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)


result = idetincal_tree(root, root2)
print(result)
