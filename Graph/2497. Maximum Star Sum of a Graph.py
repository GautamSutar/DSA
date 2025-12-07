class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        nbrs = [[] for _ in range(n)]

        for a, b in edges:
            nbrs[a].append(vals[b])
            nbrs[b].append(vals[a])

        ans = float("-inf")

        for i in range(n):
            arr = sorted((x for x in nbrs[i] if x > 0), reverse=True)
            s = vals[i] + sum(arr[:k])
            ans = max(ans, s)

        return ans
