class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


# ⏱ Time Complexity
# O(n) → single pass

# 📦 Space Complexity
# O(n) → hash map

# ✅ Why this is BEST
# Fast
# Clean
# Single pass
# Industry standard
