from collections import defaultdict


class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def dfs(root, level, levelCount):
    if root is None:
        return 
    levelCount[level] += 1
    dfs(root.left, level + 1, levelCount)
    dfs(root.right, level + 1, levelCount)

def maxNodeLevel(root):
    if root is None:
        return -1
    levelCount = defaultdict(int)
    dfs(root, 0, levelCount)
    maxNodes = 0
    maxLevel = 0
    
    for level in levelCount:
        count = levelCount[level]
        if count > maxNodes:
            maxNodes = count
            maxLevel = level
    return maxLevel


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.right.right = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.left.left.left = Node(5)
    print(maxNodeLevel(root))
    