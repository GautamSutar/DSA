class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0


# | Type  | Value    |
# | ----- | -------- |
# | Time  | **O(1)** |
# | Space | **O(1)** |
