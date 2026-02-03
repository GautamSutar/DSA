# 🔁 1) Two Pointers Pattern

## ✅ What is Two Pointers?
Two Pointers means using two indices to traverse an array (or string) instead of one.
Instead of:

```
i = 0 → n-1
```

We use:

```
left = 0
right = n-1
```

or

```
slow = 0
fast = 0
```

Both pointers move based on conditions.

## 🧠 Why Use Two Pointers?
Because it:
* Reduces time complexity
* Avoids nested loops
* Converts O(N²) → O(N)

## 🧩 When to Think of Two Pointers?
Use it when:
✔ Array or string ✔ Pairs / comparisons ✔ Reversal ✔ Removing duplicates ✔ Sorted data ✔ From both ends

If question says:
Find pair Remove duplicates Reverse Check palindrome Compare two ends
👉 Think Two Pointers

## 🔹 Common Two Pointer Styles

### 1️⃣ Opposite Direction Pointers

```
L →         ← R
[ 1, 2, 3, 4, 5 ]
```

Used when:
* Pair sum
* Reverse array
* Palindrome

### 2️⃣ Same Direction (Slow & Fast)

```
S →  
F → → →
[1,1,2,2,3]
```

Used when:
* Remove duplicates
* Move zeroes
* Filtering

## ✅ Example 1: Reverse an Array
Input: `[1,2,3,4,5]`
Idea: Swap left & right
Steps:

```
L=0, R=4 → swap
L=1, R=3 → swap
Stop when L >= R
```

Code (Python)

```python
l, r = 0, len(arr)-1
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
```

⏱ Time: O(N)
🧠 Space: O(1)

## ✅ Example 2: Pair Sum in Sorted Array
Input: `arr = [1,2,3,4,6]` `target = 6`
Logic:

```
L=0 (1)
R=4 (6)
1+6=7 → too big → R--
1+4=5 → too small → L++
2+4=6 → FOUND
```

Code

```python
l, r = 0, len(arr)-1
while l < r:
    s = arr[l] + arr[r]
    if s == target:
        return True
    elif s < target:
        l += 1
    else:
        r -= 1
```

## ✅ Example 3: Remove Duplicates (Sorted Array)
Input: `[1,1,2,2,3]`
Idea:
Slow pointer keeps unique Fast pointer scans

```
S=0
F=1 → if arr[F] != arr[S]
       S++
       arr[S]=arr[F]
```

Code

```python
s = 0
for f in range(1, len(nums)):
    if nums[f] != nums[s]:
        s += 1
        nums[s] = nums[f]
return s+1
```

## 🎯 Pattern Recognition Trick
If you see:

```
compare
pair
two ends
remove
reverse
sorted array
```

👉 Try Two Pointers FIRST.

## 🧠 Mental Template

```
Initialize pointers
While condition:
    Check
    Move left or right
Return answer
```

## ✅ Two Pointers Summary

| Feature | Value |
|---------|-------|
| Best For | Pair, reverse, cleanup |
| Time | O(N) |
| Space | O(1) |
| Uses | Left-Right OR Slow-Fast |