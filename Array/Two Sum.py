def twoSum(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        diff = target - num 
        if diff in mp:
            return (mp[diff], i)
        mp[num] = i
    return []
print(twoSum([2, 7, 11, 15], 9))

        