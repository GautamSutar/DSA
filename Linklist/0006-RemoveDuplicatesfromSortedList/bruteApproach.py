class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        seen = set()
        dummy = ListNode(0)
        tail = dummy
        curr = head

        while curr:
            if curr.val not in seen:
                seen.add(curr.val)
                tail.next = ListNode(curr.val)
                tail = tail.next
            curr = curr.next

        return dummy.next


# Works, but extra memory → not ideal for interviews.