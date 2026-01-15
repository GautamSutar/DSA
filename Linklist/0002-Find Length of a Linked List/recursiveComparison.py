# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head

        def check(right):
            if not right:
                return True
            if not check(right.next):
                return False
            is_equal = self.left.val == right.val
            self.left = self.left.next
            return is_equal
        return check(head)


# | Approach         | Time | Space  |
# | ---------------- | ---- | ------ |
# | Array            | O(n) | O(n)   |
# | Stack            | O(n) | O(n)   |
# | Reverse 2nd Half | O(n) | O(1)   |
# | Recursion        | O(n) | O(n)   |
