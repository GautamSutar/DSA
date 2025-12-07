class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = [set() for _ in range(n + 1)]
        deg = [0] * (n + 1)

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
            deg[a] += 1
            deg[b] += 1

        odd = [i for i in range(1, n + 1) if deg[i] % 2 == 1]

        if len(odd) == 0:
            return True

        if len(odd) == 2:
            a, b = odd
            if b not in adj[a]:
                return True
            for x in range(1, n + 1):
                if x != a and x != b:
                    if x not in adj[a] and x not in adj[b]:
                        return True
            return False

        if len(odd) == 4:
            a, b, c, d = odd
            if b not in adj[a] and d not in adj[c]:
                return True
            if c not in adj[a] and d not in adj[b]:
                return True
            if d not in adj[a] and c not in adj[b]:
                return True
            return False

        return False
