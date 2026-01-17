In the line dummy = ListNode(0, head), you are creating a "Dummy" or "Sentinel" node to simplify edge cases in linked list manipulation. 
What it does:
Creates a new node: It initializes a new ListNode object with a value of 0.
Points to the original list: It sets the next pointer of this new node to the head of your existing linked list.
Acts as a new starting point: Instead of your list starting at head, your temporary structure now looks like: [0] -> [head] -> [node 1] -> ... 
Why it is used here:
The primary purpose is to handle edge cases where the node to be removed is the head of the list (e.g., removing the 1st element from a 1-element list, or the 5th element from a 5-element list). 
Standard Logic: To remove a node, you need to stand at the node before it and change its next pointer.
The Problem: If you need to remove the first node (the head), there is no node before it.
The Solution: By placing a dummy node before the head, the original head now has a node preceding it. This allows the line curr.next = curr.next.next to work universally, even if curr.next is the original head