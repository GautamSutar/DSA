def uniqueNumber(nums):
    res = 0
    for num in nums:
        res ^= num 
    return res
print(uniqueNumber([4, 1, 2, 1, 2]))