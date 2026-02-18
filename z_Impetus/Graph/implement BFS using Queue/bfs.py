class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


from collections import deque


def bfs(start):
    visited = set()
    queue = deque()
    visited.add(start)
    queue.append(start)
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")


A.neighbors = [B, C]
B.neighbors = [A, D]
C.neighbors = [A, D]
D.neighbors = [B, C]
bfs(A)
