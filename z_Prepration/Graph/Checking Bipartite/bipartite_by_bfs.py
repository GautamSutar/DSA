class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


from collections import deque


def is_bipartite_graph(node):
    color = {}
    for node in nodes:
        if node not in color:
            queue = deque([node])
            color[node] = 0

            while queue:
                curr = queue.popleft()
                for neighbor in curr.neighbors:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[curr]
                        queue.append(neighbor)
                    elif color[neighbor] == color[curr]:
                        return False
    return True


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")


A.neighbors = [B, C]
B.neighbors = [A, D]
C.neighbors = [A, D]
D.neighbors = [B, C]
E.neighbors = [C, D]

nodes = [A, B, C, D, E]
print(is_bipartite_graph(nodes))
