# Dummy Node (Sentinel Node) in Linked Lists

## What is a Dummy Node?

A dummy or sentinel node is a technique used to simplify edge cases in linked list manipulation.

## Syntax
```python
dummy = ListNode(0, head)
```

## What This Does

### Creates a New Node
Initializes a new `ListNode` object with a value of `0`.

### Points to the Original List
Sets the `next` pointer of this new node to the `head` of your existing linked list.

### Acts as a New Starting Point
Instead of your list starting at `head`, your temporary structure now looks like:
```
[0] -> [head] -> [node 1] -> [node 2] -> ...
```

## Why Use a Dummy Node?

The primary purpose is to handle edge cases where the node to be removed is the head of the list.

### The Problem
- **Standard Logic**: To remove a node, you need to stand at the node before it and change its `next` pointer
- **Edge Case Issue**: If you need to remove the first node (the head), there is no node before it
- **Example Scenarios**: 
  - Removing the 1st element from a 1-element list
  - Removing the 5th element from a 5-element list (when it's also the head)

### The Solution
By placing a dummy node before the head, the original head now has a node preceding it. This allows the operation:
```python
curr.next = curr.next.next
```
to work universally, even if `curr.next` is the original head.

## Benefits
- **Eliminates special cases**: No need for separate logic to handle head removal
- **Simplifies code**: One consistent approach works for all positions
- **Cleaner implementation**: Reduces conditional statements and edge case handling

## Return Value
After manipulation, return `dummy.next` to get the (potentially new) head of the modified list.