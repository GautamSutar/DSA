def largest_number_by_concatenate(arr):
    s = ""
    for i in range(len(arr)):
        s += str(arr[i])
    return s[::-1]
arr = list(map(int, input().split()))
print(largest_number_by_concatenate(arr))
