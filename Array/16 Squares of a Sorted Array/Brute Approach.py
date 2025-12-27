class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            res.append(x * x)
        res.sort()
        return res


# ⏱ Time Complexity
# Squaring: O(n)
# Sorting: O(n log n)

# 🧠 Space Complexity
# O(n)

# ⚠️ Works, but not optimal (follow-up fails)