def alternate_max_min(arr):
    count = 0
    while len(arr) > 1:
        if count % 2 == 0:
            n = arr.pop(arr.index(max(arr)))
        else:
            n = arr.pop(arr.index(min(arr)))
        count += 1
    return arr[0]

arr = list(map(int, input().split()))
print(alternate_max_min(arr))
    