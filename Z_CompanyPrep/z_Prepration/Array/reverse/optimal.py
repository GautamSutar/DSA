def reverse_array_brute(arr):
    n = len(arr)
   
    l = 0
    r = len(arr) -1
    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l += 1
        r -= 1
    return arr


arr = [1, 2, 3, 4, 5]
print(reverse_array_brute(arr))
