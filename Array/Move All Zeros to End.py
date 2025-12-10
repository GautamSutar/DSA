def moveZeroes(nums):
    insert = 0
    for x in nums:
        if x != 0:
            nums[insert] = x
            insert += 1
    while insert < len(nums):
        nums[insert] = 0
        insert += 1
    return nums 

print(moveZeroes([0, 1, 0, 3, 12]))
