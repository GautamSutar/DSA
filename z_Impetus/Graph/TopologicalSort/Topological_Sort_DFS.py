class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        
def dfs_approach(node, visited, stack):
    visited.add(node)
    
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs_approach(neighbor, visited, stack)
    stack.append(node)

def topological_sort(nodes):
    
    visited = set()
    stack = []
    
    for node in nodes:
        if node not in visited:
            dfs_approach(node, visited, stack)
    stack.reverse()
    return [node.value for node in stack]


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

A.neighbors = [C]
B.neighbors = [C, D]
C.neighbors = [E]
D.neighbors = [F]
E.neighbors = [F]
F.neighbors = []

nodes = [A, B, C, D, E, F]

print(topological_sort(nodes))


