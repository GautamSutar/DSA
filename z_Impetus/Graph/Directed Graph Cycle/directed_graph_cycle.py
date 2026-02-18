class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def find_directed_cycle(node, visited, rec_set):

    visited.add(node)
    rec_set.add(node)

    for neighbor in node.neighbors:
        if neighbor not in visited:
            if find_directed_cycle(neighbor, visited, rec_set):
                return True
        elif neighbor in rec_set:
            return True

    rec_set.remove(node)
    return False


def cycle_detect(nodes):
    visited = set()
    rec_set = set()

    for node in nodes:
        if node not in visited:
            if find_directed_cycle(node, visited, rec_set):
                return True

    return False


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.neighbors = [B]
B.neighbors = [C]
C.neighbors = [D]
D.neighbors = [D]

nodes = [A, B, C, D]

print(cycle_detect(nodes))
