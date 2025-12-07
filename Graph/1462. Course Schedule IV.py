Brute Force Approach — DFS for Every Query (Slow)
class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(start, target):
            stack = [start]
            visited = set()
            while stack:
                node = stack.pop()
                if node == target:
                    return True
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
            return False

        return [dfs(u, v) for u, v in queries]


Better Approach — Floyd–Warshall (DP on DAG)
class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        dp = [[False] * n for _ in range(n)]

        for u, v in prerequisites:
            dp[u][v] = True

        for k in range(n):
            for i in range(n):
                if dp[i][k]:
                    for j in range(n):
                        if dp[k][j]:
                            dp[i][j] = True

        return [dp[u][v] for u, v in queries]


Optimal Approach — Topological Sort + Propagation (DAG DP)
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        prereq = [set() for _ in range(numCourses)]
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for nxt in graph[node]:
                prereq[nxt].add(node)
                prereq[nxt] |= prereq[node]
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return [u in prereq[v] for u, v in queries]
