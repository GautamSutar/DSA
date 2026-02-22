class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

import heapq
import itertools
def dijkstra(start):
    distance = {start: 0}
    prev = {}
    counter = itertools.count()
    min_heap = [(0, next(counter), start)]
    while min_heap:
        current_distance, _,current_node = heapq.heappop(min_heap)
        if current_distance > distance.get(current_node, float('inf')):
            continue
        for neighbor, weight in current_node.neighbors:
            new_distance = current_distance + weight
            if new_distance < distance.get(neighbor, float('inf')):
                distance[neighbor] = new_distance
                prev[neighbor] = current_node
                heapq.heappush(min_heap, (new_distance, next(counter), neighbor))
    return distance, prev
                

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")


A.neighbors = [(B, 1), (C, 4)]
B.neighbors = [(C, 2), (D, 5)]
C.neighbors = [(D, 1)]
D.neighbors = []

distance, prev = dijkstra(A)
for node, dist in distance.items():
    print(f"Node -> {node.value}:{dist}")
