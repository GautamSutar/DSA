from collections import deque
def reverse(q, k):
    d = deque()
    for _ in range(k):
        d.appendleft(q.popleft())
    while d:
        q.append(d.popleft())
    for _ in range(len(q) - k):
        q.append(q.popleft())
arr = list(map(int, input("Enter queue element:").split()))
k = int(input("Enter the k position of reverse: "))
q = deque(arr)
reverse(q, k)
print(*q)