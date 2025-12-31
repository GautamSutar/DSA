class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        return cleaned == cleaned[::-1]

# ⏱️ Complexity

# Time: O(n)

# Space: O(n)

# 🟡 Good, but extra space