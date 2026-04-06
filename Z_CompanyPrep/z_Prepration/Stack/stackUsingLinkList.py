class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(new_node.data)

    def pop(self):
        if self.isEmpty():
            print("UnderFlow")
            return None
        removed = self.top.data
        self.top = self.top.next.next
        print("Removed Data: ", removed)

    def peek(self):
        if self.isEmpty():
            print("Empty")
        print("Peek: ", self.top.data)

    def isEmpty(self):
        return self.top is None


obj = Stack()
obj.push(10)
obj.push(20)
obj.peek()
obj.push(30)
obj.pop()
