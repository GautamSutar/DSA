from collections import defaultdict, deque


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i != j:
                    x2, y2, _ = bombs[j]
                    if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1**2:
                        graph[i].append(j)

        def bfs(start):
            visited = set([start])
            q = deque([start])
            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            return len(visited)

        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
        return ans
