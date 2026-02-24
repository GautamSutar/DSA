class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
def reverLinkList(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

head = Node(5)
head.next = Node(10)
head.next.next = Node(11)
head.next.next.next = Node(20)
head.next.next.next.next = Node(25)

result = reverLinkList(head)

while result:
    print(result.data)
    result = result.next



