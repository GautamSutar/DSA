class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return True

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        return False


def has_cycle_union_find(nodes):
    ds = DisjointSet()
    for node in nodes:
        ds.parent[node] = node
        ds.rank[node] = 0

    visited_edges = set()
    for node in nodes:
        for neighbor in node.neighbors:
            if (neighbor, node) in visited_edges:
                continue
            if ds.union(node, neighbor):
                return True

            visited_edges.add((node, neighbor))


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.neighbors = [B, C]
B.neighbors = [A, D]
C.neighbors = [A, D]
D.neighbors = [B, C]

nodes = [A, B, C, D]
print(has_cycle_union_find(nodes))
