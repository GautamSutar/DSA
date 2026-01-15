class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        middle = count // 2  # correct middle

        curr = head
        for _ in range(middle - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head


# ⏱ Complexity

# Time: O(n) ⭐

# Space: O(1) ⭐
