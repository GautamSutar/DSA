class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        deg = [0] * (n + 1)
        adj = [[False] * (n + 1) for _ in range(n + 1)]
        for u, v in edges:
            adj[u][v] = True
            adj[v][u] = True
            deg[u] += 1
            deg[v] += 1

        INF = float("inf")
        ans = INF
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if adj[i][j]:
                    for k in range(j + 1, n + 1):
                        if adj[i][k] and adj[j][k]:
                            degree = (deg[i] - 2) + (deg[j] - 2) + (deg[k] - 2)
                            ans = min(ans, degree)

        return ans if ans != INF else -1
