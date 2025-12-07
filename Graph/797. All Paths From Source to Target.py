Brute Force Approach — DFS Without Backtracking
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []

        def dfs(node, path):
            if node == n - 1:
                res.append(path[:])
                return
            for nei in graph[node]:
                dfs(nei, path + [nei])  # Creates many new lists (inefficient)

        dfs(0, [0])
        return res


Better Approach — DFS With Backtracking
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        path = [0]

        def dfs(node):
            if node == n - 1:
                res.append(path[:])
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei)
                path.pop()

        dfs(0)
        return res

Optimal Approach — BFS Level-Order Traversal
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = deque()
        q.append([0])
        res = []

        while q:
            path = q.popleft()
            node = path[-1]

            if node == n - 1:
                res.append(path)
                continue

            for nei in graph[node]:
                q.append(path + [nei])

        return res

