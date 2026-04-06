def average(nums, k):
    avg = 0
    size = len(nums)
    total = 0
    max_avg = 0
    if size == k:
        avg = sum(nums) / k 
        return avg 
    for i in range(size - k + 1):
        for j in range(i, k + i):
            total += nums[j]
        avg = total / k
        if avg > max_avg:
            max_avg = avg
        total = 0
    return max_avg
    
    
    
print(average([1,12,-5,-6,50,3], 4))




