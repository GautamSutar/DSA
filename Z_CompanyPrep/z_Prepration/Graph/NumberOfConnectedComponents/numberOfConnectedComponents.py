class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def dfs(node, visited):
    visited.add(node)

    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited)


def count_component(nodes):
    visited = set()
    count = 0
    for node in nodes:
        if node not in visited:
            dfs(node, visited)
            count += 1
    return count


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
A.neighbors = [B, C]
B.neighbors = [A]
C.neighbors = [A]
D.neighbors = [E]
E.neighbors = [D]
F.neighbors = []

nodes = [A, B, C, D, E, F]
print(count_component(nodes))
