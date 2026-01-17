class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = []
        curr = head 
        while curr:
            node.append(curr)
            curr = curr.next
        return node[len(node) // 2]
    
# | Metric | Value    |
# | ------ | -------- |
# | Time   | **O(N)** |
# | Space  | **O(N)** |
