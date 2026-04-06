class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    
def lca(root, p, q):
    if not root:
        return None
    
    if root == p or root == q:
        return root
    
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    
    if left and right:
        return root
            
    return left if left else right



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
node4 = root.left.left
node5 = root.left.right

result = lca(root, node4, node5)
print(result.val)
