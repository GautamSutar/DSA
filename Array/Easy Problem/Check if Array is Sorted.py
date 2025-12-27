def isSorted(nums):
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))

print(isSorted([1, 2, 3, 4]))
print(isSorted([4, 5, 2, 1]))