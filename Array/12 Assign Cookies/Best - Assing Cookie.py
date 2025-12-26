class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0  # pointer for children
        j = 0  # pointer for cookies
        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count


# | Step         | Complexity              |
# | ------------ | ----------------------- |
# | Sorting      | O(n log n + m log m)    |
# | Two pointers | O(n + m)                |
# | **Total**    | O(n log n + m log m)    |
