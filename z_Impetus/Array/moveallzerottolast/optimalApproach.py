def move_zeroes_optimal(arr):
    n = len(arr)
    j = 0  # position for next non-zero

    for i in range(n):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1

    return arr

# Example
arr = [0, 1, 0, 3, 12]
print(move_zeroes_optimal(arr))
