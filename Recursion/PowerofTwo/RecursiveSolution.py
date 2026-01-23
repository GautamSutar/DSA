class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def power(n):
            if n <= 0:
                return False
            if n == 1:
                return True
            if n % 2 != 0:
                return False
            return self.isPowerOfTwo(n // 2)

        return power(n)



# Complexity

# Time: O(log n)

# Space: O(log n) (recursion stack)