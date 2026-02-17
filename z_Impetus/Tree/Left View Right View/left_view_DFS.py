
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    
def left_view_dfs(root):
    result = []
    
    def helper(node, level):
        if not node:
            return
        
        if level == len(result):
            result.append(node.val)
        
        helper(node.left, level + 1)
        helper(node.right, level + 1)
    
    helper(root, 0)
    return result
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.right.right = Node(6)
answer = left_view_dfs(root)
print(answer)