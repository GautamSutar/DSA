def frequency(nums):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    return freq

print(frequency([1, 2, 2, 3, 3, 3]))  
