class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        for a, b in roads:
            deg[a] += 1
            deg[b] += 1

        deg.sort()
        importance = 0
        val = 1

        for d in deg:
            importance += d * val
            val += 1

        return importance
