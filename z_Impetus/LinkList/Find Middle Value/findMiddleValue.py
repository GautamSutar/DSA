class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

head = Node(5)
head.next = Node(10)
head.next.next = Node(11)
head.next.next.next = Node(12)

result = find_middle(head)
print(f"Middle Value: {result.data}")



