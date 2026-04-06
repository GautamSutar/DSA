def mean(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum // len(arr)

arr = list(map(int, input().split()))

print(mean(arr))
