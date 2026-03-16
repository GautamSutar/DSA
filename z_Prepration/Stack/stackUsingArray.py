# stack [1, 2, 3, 4, 5]
#


class StackUsingArray:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.top = -1

    def push(self, number):
        if self.top == self.size - 1:
            print("Overflow Stack")
        self.top += 1
        self.arr[self.top] = number

    def pop(self):
        if self.top == -1:
            print("Underflow Stack")
        self.top -= 1
        self.arr.pop()

    def peek(self):
        print("Value: ", self.arr[-1])

    def print(self):
        print(self.arr)


size = int(input("Enter the size of the array: "))
obj = StackUsingArray(size)
for i in range(1, size + 1):
    obj.push(i)
# obj.pop()
obj.peek()
obj.print()


# 🧠 OOPS Concepts Used (Interview Explanation)
# 1️⃣ Class and Object

# Node class

# Stack class

# s = Stack() → object creation

# 2️⃣ Encapsulation

# Data members:

# top

# size

# are hidden inside Stack class.

# 3️⃣ Abstraction

# User only interacts with:

# push()

# pop()

# peek()

# Internal linked list logic hidden.

# 4️⃣ Composition (Important Advanced Point ⭐)

# Stack uses Node objects inside it.

# This is called:
# 👉 "Has-A relationship"
# Stack HAS nodes.

# ⚡ Why Linked List Stack is Better than Array Stack?
# Array Stack	Linked List Stack
# Fixed size	Dynamic size
# Overflow possible	No overflow (until memory full)
# Wastes space	Efficient memory use
# ⏱ Time Complexity
# Operation	Complexity
# push	O(1)
# pop	O(1)
# peek	O(1)
# 🎯 Interview Smart Answer

# "Sir, I implemented stack using singly linked list.
# Insertion and deletion happen at head for O(1) time complexity.
# I used OOPS concepts like class, object, encapsulation, abstraction and composition.
# Unlike array stack, this implementation supports dynamic size."