Brute Force DFS (Cycle Detection Per Node — Very Slow)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        def hasCycle(node, visited):
            if node in visited:
                return True
            visited.add(node)
            for nei in graph[node]:
                if hasCycle(nei, visited):
                    return True
            visited.remove(node)
            return False

        safe = []
        for i in range(n):
            if not hasCycle(i, set()):
                safe.append(i)
        return safe

Better DFS Approach (Memoization + Coloring)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n     # 0=unvisited, 1=visiting, 2=safe

        def dfs(node):
            if color[node] != 0:
                return color[node] == 2
            color[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            color[node] = 2
            return True

        return [i for i in range(n) if dfs(i)]

Optimal Approach (Reverse Graph + Topological Sort using Kahn's Algorithm)

from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        rev = [[] for _ in range(n)]
        indegree = [0] * n

        for u in range(n):
            for v in graph[u]:
                rev[v].append(u)
            indegree[u] = len(graph[u])

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True
            for prev in rev[node]:
                indegree[prev] -= 1
                if indegree[prev] == 0:
                    q.append(prev)

        return [i for i in range(n) if safe[i]]
