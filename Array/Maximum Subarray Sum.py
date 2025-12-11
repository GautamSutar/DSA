def maxSubArray(nums):
    best = curr = nums[0]
    for x in nums[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)
    return best


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    