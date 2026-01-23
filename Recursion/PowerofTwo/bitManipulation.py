class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

# Complexity

# Time: O(1)

# Space: O(1)

# ✅ This is the expected interview solution

