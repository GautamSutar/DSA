Brute Force Approach (DFS from every node)
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)

        def dfs(start, target):
            stack = [start]
            visited = set()
            while stack:
                node = stack.pop()
                if node == target:
                    return True
                for prev in graph[node]:
                    if prev not in visited:
                        visited.add(prev)
                        stack.append(prev)
            return False

        ans = [[] for _ in range(n)]
        for target in range(n):
            for start in range(n):
                if start != target and dfs(start, target):
                    ans[target].append(start)

        for lst in ans:
            lst.sort()

        return ans

Better Approach — DFS from each node with memoization
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)

        memo = {}
        
        def dfs(node):
            if node in memo:
                return memo[node]
            s = set()
            for prev in graph[node]:
                s.add(prev)
                s |= dfs(prev)
            memo[node] = s
            return s

        ans = []
        for i in range(n):
            arr = sorted(dfs(i))
            ans.append(arr)

        return ans


Optimal Approach — Topological Order + DP Propagation
from collections import deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        q = deque([i for i in range(n) if indegree[i] == 0])
        ancestors = [set() for _ in range(n)]

        while q:
            node = q.popleft()
            for nxt in graph[node]:
                ancestors[nxt].add(node)
                ancestors[nxt] |= ancestors[node]
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return [sorted(list(a)) for a in ancestors]
