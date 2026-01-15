# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        curr = head
        middle = count // 2
        for _ in range(middle):
            curr = curr.next
        return curr


# | Metric | Value               |
# | ------ | ------------------- |
# | Time   | **O(N)** (2 passes) |
# | Space  | **O(1)**            |
