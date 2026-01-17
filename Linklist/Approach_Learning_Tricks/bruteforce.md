# Find Middle Node of Linked List

## Algorithm Overview
This algorithm finds the middle node of a linked list using a counting approach.

## Approach

### Variables Needed
- **curr**: Pointer to traverse the linked list
- **count**: Counter to track the size of the linked list
- **middle**: Stores the middle index position

### Process
1. Use a `while` loop to traverse the linked list with `curr` pointer
2. Count the total size of the linked list by checking each `curr` node
3. After counting, reset `curr` to `head` to start from the beginning
4. Calculate `middle` position (typically `count // 2`)
5. Use a `for` loop to iterate until reaching the `middle` position
6. Return the node at the middle position

## Key Concept
This two-pass approach first determines the total length of the linked list, then traverses again to reach the exact middle position. The middle node is found at position `count // 2`.

## Time Complexity
O(n) - Two passes through the linked list