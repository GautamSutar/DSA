import heapq


def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


arr = [5, 2, 9, 1, 5, 6]

print(heap_sort(arr))
