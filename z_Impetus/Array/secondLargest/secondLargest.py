def secondLargest(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    largest = arr[n - 1]
    for i in range(n - 1, -1, -1):
        if arr[i] != largest or arr[i] < largest:
            return arr[i]


arr = [10, 5, 20, 8]
print(secondLargest(arr))
