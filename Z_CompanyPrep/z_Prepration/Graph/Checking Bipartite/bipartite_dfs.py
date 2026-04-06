class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []




def dfs(node, color, current_color):
    color[node] = current_color

    for neighbor in node.neighbors:
        if neighbor not in color:
            if not dfs(neighbor, color, 1 - current_color):
                return False
        elif color[neighbor] == current_color:
            return False

    return True


def is_bipartite_dfs(nodes):
    color = {}

    for node in nodes:
        if node not in color:
            if not dfs(node, color, 0):
                return False

    return True

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

A.neighbors = [B, C]
B.neighbors = [A, D]
C.neighbors = [A, E]
D.neighbors = [B, E]
E.neighbors = [D, C]
nodes = [A, B, C, D, E]
print(is_bipartite_dfs(nodes))
