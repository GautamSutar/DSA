class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


# ⏱ Time Complexity
# O(n²) → two nested loops

# 📦 Space Complexity
# O(1) → no extra memory