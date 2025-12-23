class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        prefix_sum = 0
        min_prefix = 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_prefix)
            min_prefix = min(min_prefix, prefix_sum)

        return max_sum
    
    
# ⏱ Time Complexity
# O(n)

# 📦 Space Complexity
# O(1)

# ✔️ Efficient
# ❌ Slightly less intuitive