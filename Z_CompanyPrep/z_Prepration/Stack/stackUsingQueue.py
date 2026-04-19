class Stack








# 📌 Implement Stack Using Queues (LIFO using FIFO)

# Stack = LIFO
# Queue = FIFO

# 👉 Goal: Use Queue operations (enqueue, dequeue) to behave like a Stack.

# There are 2 common approaches:

# 1️⃣ Costly Push (Push O(n), Pop O(1))
# 2️⃣ Costly Pop (Push O(1), Pop O(n))

# We’ll implement Costly Push (Single Queue) – Most asked in interviews 🔥

# 🔹 Visual Idea (Costly Push Method)

# When pushing:

# Insert element into queue

# Rotate previous elements behind it

# So newest element always comes to front
# 🧠 Dry Run (Push 10, 20, 30)

# Queue state after each push:

# Push 10
# [10]

# Push 20
# Append → [10, 20]
# Rotate once → [20, 10]

# Push 30
# Append → [20, 10, 30]
# Rotate twice → [30, 20, 10]

# Now front = 30 → behaves like stack top ✔

# ⏱ Time Complexity
# Operation	Complexity
# push	O(n)
# pop	O(1)
# peek	O(1)
# 🧠 OOPS Concepts Used

# ✔ Class & Object
# ✔ Encapsulation
# ✔ Abstraction
# ✔ Constructor

# We encapsulated queue inside stack class.

# 🎯 Interview Smart Answer

# "Sir, I implemented stack using a single queue.
# Push operation is costly (O(n)) because we rotate the queue to maintain LIFO order.
# Pop and peek are O(1).
# This demonstrates understanding of abstract data type transformation."

# 🔥 If Interviewer Asks Follow-Up
# ❓ Can we make push O(1)?

# Yes → Use two queues
# Then pop becomes O(n).