def second_largest_optimal(arr):
    largest = -(10**9)
    second_largest = -(10**9)

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == -(10**9):
        return -1

    return second_largest


# Example
arr = [10, 5, 20, 8]
print(second_largest_optimal(arr))
