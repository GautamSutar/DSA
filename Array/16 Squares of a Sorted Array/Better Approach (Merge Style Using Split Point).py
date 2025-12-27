class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        right = 0
        while right < n and nums[right] < 0:
            right += 1

        left = right - 1
        while left >= 0 and right < n:
            if nums[left] * nums[left] < nums[right] * nums[right]:
                res.append(nums[left] * nums[left])
                left -= 1
            else:
                res.append(nums[right] * nums[right])
                right += 1

        while left >= 0:
            res.append(nums[left] * nums[left])
            left -= 1

        while right < n:
            res.append(nums[right] * nums[right])
            right += 1

        return res

# ⏱ Time Complexity
# O(n)

# 🧠 Space Complexity
# O(n)