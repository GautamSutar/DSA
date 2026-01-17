# Delete Nth Node from End of Linked List

## Problem Overview
Given a linked list and a value `n`, delete the nth node from the end of the list.

## Algorithm Approach

### Step 1: Calculate Length
First, traverse the entire linked list to calculate its total length.

### Step 2: Find Target Position
Subtract `n` from the length to find the position of the node to delete from the beginning.
```
target_position = length - n
```

### Step 3: Traverse to Target
Use a `for` loop to traverse to the node just before the target position.

### Step 4: Remove Node
Update the `next` pointer of the current node to skip the target node:
```python
curr.next = curr.next.next
```

## Example
If we have a list: `1 -> 2 -> 3 -> 4 -> 5` and `n = 2`
- Length = 5
- Target position from start = 5 - 2 = 3 (node with value 4)
- Traverse to position 2 (node with value 3)
- Update: `3.next = 3.next.next` (skip node 4)
- Result: `1 -> 2 -> 3 -> 5`

## Key Variables
- **length**: Total number of nodes in the linked list
- **n**: Position from the end to delete
- **curr**: Pointer to traverse the list
- **target_position**: Calculated position from the start (length - n)

## Time Complexity
O(n) - Two passes through the linked list (one to count, one to delete)