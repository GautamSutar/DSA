# Delete Middle Node of Linked List

## Algorithm Overview
This algorithm uses the two-pointer technique to find and delete the middle node of a linked list.

## Approach

### Pointers
- **slow**: Moves one step at a time
- **fast**: Moves two steps at a time
- Both pointers start at the **head**

### Process
1. Initialize both `slow` and `fast` pointers to `head`
2. Use a `while` loop to traverse the list, checking `fast` pointer
3. In each iteration:
   - `slow` moves one step forward
   - `fast` moves two steps forward
4. When `fast` reaches the end, `slow` will be at the middle node
5. Return `slow` pointer (points to the middle node)

## Key Concept
The fast pointer moves twice as fast as the slow pointer. When the fast pointer reaches the end of the list, the slow pointer will be positioned at the middle node, making it ready for deletion.