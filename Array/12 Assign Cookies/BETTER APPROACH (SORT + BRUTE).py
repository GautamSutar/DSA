class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        used = [False] * len(s)
        count = 0

        for i in range(len(g)):
            for j in range(len(s)):
                if not used[j] and s[j] >= g[i]:
                    used[j] = True
                    count += 1
                    break

        return count



# ⏱ Time Complexity
# Sorting: O(n log n + m log m)
# Matching: O(n × m) ❌
# ❌ Still slow for large input