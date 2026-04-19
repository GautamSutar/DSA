def find_duplicates_optimal_freq(arr):
    n = len(arr)
    freq = [0] * (n + 1)

    for num in arr:
        freq[num] += 1

    for i in range(1, n + 1):
        if freq[i] > 1:
            print(i)


# Example
arr = [1, 2, 3, 1, 3, 6, 6]
find_duplicates_optimal_freq(arr)
