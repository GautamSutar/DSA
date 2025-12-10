def rotate(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))