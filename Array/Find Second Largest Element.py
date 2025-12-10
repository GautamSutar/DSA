def secondLargest(nums):
    nums = list(set(nums))
    nums.sort()
    if len(nums) < 2:
        return None 
    return nums[-2]

print(secondLargest([3, 5, 2, 9, 1]))
