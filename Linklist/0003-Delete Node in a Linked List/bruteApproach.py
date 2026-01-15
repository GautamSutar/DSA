class Solution:
    def deleteNode(self, head, node):
        if head == node:
            head = head.next
            return

        prev = None
        curr = head

        while curr != node:
            prev = curr
            curr = curr.next

        prev.next = curr.next


# Time: O(n)
# Space: O(1)
