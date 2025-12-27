class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums

# ⏱ Time Complexity
# Squaring: O(n)
# Sorting: O(n log n)

# 🧠 Space Complexity
# O(1)
