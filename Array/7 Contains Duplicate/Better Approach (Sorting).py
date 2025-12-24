class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


# ⏱ Time Complexity
# O(n log n)

# 📦 Space Complexity
# O(1) (ignoring sort internals)

# ✔️ Cleaner
# ❌ Modifies input