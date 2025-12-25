class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

# ⏱ Time Complexity
# O(n log n)

# 📦 Space Complexity
# O(1)