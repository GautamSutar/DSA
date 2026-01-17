class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        a, b = headA, headB

        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a


# Time & Space

# Time: O(m + n)

# Space: O(1)

# ✅ No extra memory

# ✅ No modification of lists