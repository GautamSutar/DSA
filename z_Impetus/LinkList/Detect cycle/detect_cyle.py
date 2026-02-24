class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
def detect_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True 
   
    
    return False

head = Node(5)
head.next = Node(10)
head.next.next = Node(11)
head.next.next.next = Node(20)
head.next.next.next.next = Node(25)
head.next.next.next.next.next = head.next
print(f"Cycle Detected: {detect_cycle(head)}")



