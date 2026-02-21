class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


from collections import deque


def count_component(node):
    visited = set()
    count = 0
    for node in nodes:
        if node not in visited:
            count += 1
            queue = deque([node])
            visited.add(node)
            while queue:
                curr = queue.popleft()
                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
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
