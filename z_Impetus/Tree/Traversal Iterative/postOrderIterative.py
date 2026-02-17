class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def inorder_iterative(root):
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

inorder_iterative(root)
