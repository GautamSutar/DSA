def missing_number_brute(arr, n):
    for num in range(min(arr), max(arr) + 1):
        found = False
        for i in range(len(arr)):
            if arr[i] == num:
                found = True
                break
        if not found:
            return num
    return -1

arr = [10, 11, 12, 14]
print(missing_number_brute(arr, 5))
