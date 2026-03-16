def find_duplicates_brute(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                print(arr[i])
                break



arr = [1, 2, 3, 1, 3, 6, 6]
find_duplicates_brute(arr)
