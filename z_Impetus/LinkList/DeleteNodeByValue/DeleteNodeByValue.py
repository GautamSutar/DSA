class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy 
    second = dummy 
   
    for i in range(n + 1):
        first = first.next 
    while first:
        first = first.next 
        second = second.next 
    second.next = second.next.next
    return dummy.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


head = remove_nth_from_end(head, 2)
while head:
    print(head.data)
    head = head.next
    
    