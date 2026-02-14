def find_peak_brute(arr):
    n = len(arr)

    for i in range(n):
        print("i", i)
        left = arr[i - 1] if i > 0 else float("-inf")
        print("left", left)
        right = arr[i + 1] if i < n - 1 else float("-inf")
        print("right", right)
        if arr[i] > left and arr[i] > right:
            return i

    return None


arr = [1, 2, 3, 1]
print(find_peak_brute(arr))
