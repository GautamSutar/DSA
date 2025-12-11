def pairSum(nums, target):
    nums.sort()
    i, j = 0, len(nums) - 1
    s = 0
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return (nums[i], nums[j])
        if s < target:
            i += 1
        else:
            j -= 1


print(pairSum([10, 5, 2, 8],10))
