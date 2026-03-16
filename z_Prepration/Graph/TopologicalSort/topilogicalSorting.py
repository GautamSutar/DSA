class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
     

from collections import deque     
    
def topological_sort_kahn(nodes):
    in_degree = {node:0 for node in nodes}

    for node in nodes:
        for neighbor in node.neighbors:
            in_degree[neighbor] += 1
    
    queue = deque()
    
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)
    
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node.value)
        
        for neighbor in node.neighbors:
            in_degree[neighbor] -= 1 
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            
    if len(topo_order) != len(nodes):
        return "Cycle detected! No Topological Ordering"
    
    return topo_order

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

print(topological_sort_kahn(nodes))


