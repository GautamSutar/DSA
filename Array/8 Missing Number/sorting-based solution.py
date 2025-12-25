class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1

        return len(nums)



# | Approach Type      | Yes / No  | 
# | ------------------ | --------  |
# | Brute force        | ❌        |
# | Hashing            | ❌        |
# | **Sorting-based**  | ✅        |
# | Math (sum formula) | ❌        |
# | XOR                | ❌        |
# | Optimal            | ❌        |
