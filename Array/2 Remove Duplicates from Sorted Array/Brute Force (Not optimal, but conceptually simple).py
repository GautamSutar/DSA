class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)


# Time Complexity
# O(n²) (because num in unique is linear)

# Space Complexity
# O(n) (extra list)

# ❌ Interviewers won’t accept this as final.