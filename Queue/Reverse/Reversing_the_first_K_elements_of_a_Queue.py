from collections import deque
def reverse_first_k(q,k):
    move_k_to_end(q,k)
    size = len(q) - k 
    for _ in range(size):
        x = q.popleft()
        q.append(x)
    return q

def move_k_to_end(q,k):
    if(k == 0):
        return
    e = q.popleft()
    move_k_to_end(q, k - 1)
    q.append(e)



n = int(input("Enter the size of the queue: "))
arr = list(map(int, input("Enter the element: ").split()))
q = deque(arr)
print(f'original array: {arr}')
k = int(input("Enter first reverse k value: "))
queue = reverse_first_k(q, k)
while queue:
    print(queue.popleft(), end=" ")