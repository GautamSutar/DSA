from collections import deque
def reverseFirstK(q, k):
    if not q or k > len(q):
        return 
    if k < 0:
        return 
    s = []
    for _ in range(k):
        s.append(q.popleft())
    for _ in range(len(s)):
        q.append(s.pop())
    for _ in range(len(q) - k):
        q.append(q.popleft())

def printq(q):
    while q:
        print(q.popleft(), end=' ') 

if __name__ == '__main__':
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    q.append(5)
k = 3
reverseFirstK(q, k)
printq(q)