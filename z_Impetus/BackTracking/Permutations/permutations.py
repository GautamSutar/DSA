def generate_subset(nums):
    result = []
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return 
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    
    # checking
    backtrack(0)
    return result
    

print(generate_subset([1, 2, 3]))

