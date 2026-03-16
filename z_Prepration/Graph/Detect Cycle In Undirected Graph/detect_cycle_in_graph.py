class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


from collections import deque


def dfs_cycle(node, visited, parent):
    visited.add(node)

    for neighbor in node.neighbors:
        if neighbor not in visited:
            if dfs_cycle(neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True

    return False


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")


A.neighbors = [B, C]
B.neighbors = [A, D]
C.neighbors = [A, D]
D.neighbors = [B, C]

visited = set()

dfs_cycle(A, visited, parent=None)

for node in visited:
    print(node.val)
