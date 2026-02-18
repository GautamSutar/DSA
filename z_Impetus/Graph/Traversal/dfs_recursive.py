class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def dfs_recursive(node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
    print(node.value, end=" ")
    visited.add(node)

    for neighbor in node.neighbors:
        dfs_recursive(neighbor, visited)


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")


A.neighbors = [B, C]
B.neighbors = [A, D]
C.neighbors = [A, D]
D.neighbors = [B, C]
dfs_recursive(A)
