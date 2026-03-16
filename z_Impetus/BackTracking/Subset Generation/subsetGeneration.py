def generate_subset(nums):
    result = []
    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return 
        current.append(nums[index])
        backtrack(index + 1, current)
        
        current.pop()
        backtrack(index + 1, current)
    
    # checking
    backtrack(0, [])
    return result
    

print(generate_subset([1,2]))


# result = [[1,2], [1], [2], []]
#  0 ->             []
#  1 ->       1           []
#  2 ->  12    1        2   []
# 
# 
# 