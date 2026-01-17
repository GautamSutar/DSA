# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a = headA
        while a:
            b = headB
            while b:
                if a is b:
                    return a
                b = b.next
            a = a.next
        return None


# Time & Space

# Time: O(m * n)

# Space: O(1)

# ❌ Too slow → interviewer will reject.