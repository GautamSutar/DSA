def average(nums, k):
    size = len(nums)
    arr = nums.copy()
    total = 0
    n = k 
    if k < 0:
        for i in range(size):
            total = nums[n] + nums[n + 1]
            arr[i] = total 
            total = 0
            n = n + 1 
        return arr
    if k == 0:
        for i in range(size):
            arr[i] = 0
        return arr
    for i in range(size):
        for j in range(size):
            if nums[j] != nums[i]:
                total += nums[j]
        arr[i] = total
        total = 0
    return arr
    
    
    
print(average([2,4,9,3], -2))




