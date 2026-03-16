def next_greater_element(nums):
    stack = []
    size = len(nums)
    result = [-1] * size 
    for i in range(size - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
        
    return result
 
print(next_greater_element([4, 5, 2, 10, 8]))
