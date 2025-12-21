class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort(key=lambda x: x[0])

        left, right = 0, len(arr) - 1

        while left < right:
            s = arr[left][0] + arr[right][0]
            if s == target:
                return [arr[left][1], arr[right][1]]
            elif s < target:
                left += 1
            else:
                right -= 1


# ⏱ Time Complexity
# Sorting: O(n log n)
# Two pointers: O(n)
# Overall: O(n log n)

# 📦 Space Complexity
# O(n) (for storing indices)

# ⚠️ Drawback
# Sorting changes order
# Slightly complex compared to hashing
