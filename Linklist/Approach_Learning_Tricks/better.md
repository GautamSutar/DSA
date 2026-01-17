# Delete Middle Node Using List Storage

## Algorithm Overview
This algorithm finds and deletes the middle node of a linked list by storing all nodes in a list structure.

## Approach

### Requirements
- **Node list**: An array/list to store linked list nodes
- **curr pointer**: Points to the head of the linked list

### Process
1. Initialize `curr` pointer to `head`
2. Traverse the linked list and append each `curr` node to the list
3. Once all nodes are stored, calculate the middle index (half of list length)
4. Return the node at the middle position from the stored list

## Key Concept
By storing all nodes in a list data structure, we can directly access the middle node using index-based access. The middle node is located at `list[len(list) // 2]`, which can then be removed by adjusting the previous node's next pointer.

## Space Complexity Note
This approach uses O(n) extra space to store all nodes in the list.