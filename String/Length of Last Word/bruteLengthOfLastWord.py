def lengthOfLastWord(s: str) -> int:
    words = s.split()
    print(words)
    print(f"{words[-1]}")
    return len(words[-1])


print(lengthOfLastWord(" hi   day"))

# ⏱️ Complexity

# Time: O(n)

# Space: O(n)

# 🟡 Simple but uses extra space