class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        count = 0

        while i < n - count:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                count += 1
            else:
                i += 1



# ⏱ Time Complexity
# pop() is O(n)
# Worst case: O(n²)

# 🧠 Space Complexity
# O(1) (in-place)