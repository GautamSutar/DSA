# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


# ⏱ Complexity

# Time: O(1) ⭐

# Space: O(1) ⭐

# | Approach              | Allowed | Time | Space  |
# | --------------------- | ------- | ---- | ------ |
# | Brute (using head)    | ❌       | O(n) | O(1)   |
# | Value Shifting        | ✅       | O(n) | O(1)   |
# | Copy Next Node (BEST) | ✅       | O(1) | O(1) ⭐ |
