from collections import defaultdict
import bisect


class Solution:
    def countPairs(
        self, n: int, edges: List[List[int]], queries: List[int]
    ) -> List[int]:
        deg = [0] * (n + 1)
        shared = defaultdict(int)

        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            if u > v:
                u, v = v, u
            shared[(u, v)] += 1

        arr = sorted(deg[1:])
        ans = []

        for q in queries:
            count = 0
            l, r = 0, n - 1
            while l < r:
                if arr[l] + arr[r] > q:
                    count += r - l
                    r -= 1
                else:
                    l += 1

            for (u, v), w in shared.items():
                if deg[u] + deg[v] > q and deg[u] + deg[v] - w <= q:
                    count -= 1

            ans.append(count)

        return ans
