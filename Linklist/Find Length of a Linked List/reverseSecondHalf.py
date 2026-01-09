# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        right, left = prev, head
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True


# ⏱ Complexity

# Time: O(n)

# Space: O(1) ✅