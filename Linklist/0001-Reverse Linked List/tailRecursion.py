# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        def helper(curr, prev):
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            return helper(next_node, curr)

        return helper(head, None)


# ⏱ Complexity

# Time: O(n)

# Space: O(n)


| Approach               | Time | Space | Interview Use |
| ---------------------- | ---- | ----- | ------------- |
| Iterative (3 pointers) | O(n) | O(1)  | ⭐⭐⭐⭐⭐  |
| Recursive              | O(n) | O(n)  | ⭐⭐⭐⭐     |
| Stack                  | O(n) | O(n)  | ⭐⭐          |
| Tail Recursive         | O(n) | O(n)  | ⭐⭐⭐        |
