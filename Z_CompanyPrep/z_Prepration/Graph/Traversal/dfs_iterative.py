class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def dfs_iterative(start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node.value, end=" ")
            visited.add(node)

        for neighbor in reversed(node.neighbors):
            if neighbor not in visited:
                stack.append(neighbor)


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")


A.neighbors = [B, C]
B.neighbors = [A, D]
C.neighbors = [A, D]
D.neighbors = [B, C]
dfs_iterative(A)
