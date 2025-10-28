from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set([source])
        q = deque([source])

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei == destination:
                    return True
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return False
