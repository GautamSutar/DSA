class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    curr_sum = nums[i] + nums[j] + nums[k]

                    if abs(curr_sum - target) < abs(closest - target):
                        closest = curr_sum

        return closest

# ⏱ Time Complexity
# O(n³) → 3 nested loops

# 🧠 Space Complexity
# O(1) → no extra space