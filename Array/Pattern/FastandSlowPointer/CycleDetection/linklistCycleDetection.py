while fast and fast.next:
    fast = fast.next.next
    if slow == fast:
        return True
    else:
        slow = slow.next