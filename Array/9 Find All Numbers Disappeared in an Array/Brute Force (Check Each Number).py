class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for i in range(1, n + 1):
            if i not in nums:
                result.append(i)

        return result


# ⏱ Time Complexity
# O(n²) ❌

# 📦 Space Complexity
# O(1) (excluding output)