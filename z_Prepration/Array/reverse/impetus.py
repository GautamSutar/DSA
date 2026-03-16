def reverse_array_brute(arr):
    n = len(arr)
    result = [0] * n

    j = 0
    for i in range(n - 1, -1, -1):
        result[j] = arr[i]
        j += 1

    return result


arr = [1, 2, 3, 4, 5]
print(reverse_array_brute(arr))



