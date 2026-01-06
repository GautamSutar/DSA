class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []

        for ch in s:
            if ch.isupper():
                result.append(ch.lower())
            else:
                result.append(ch)

        return "".join(result)
ob = Solution()
print(ob.toLowerCase("Hello World!"))

# ⏱️ Complexity

# Time: O(n)

# Space: O(n)