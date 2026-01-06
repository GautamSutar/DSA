class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []

        for ch in s:
            if "A" <= ch <= "Z":
                print(ch)
                result.append(chr(ord(ch) + 32))
                print(result)
            else:
                result.append(ch)

        return "".join(result)


ob = Solution()
print(ob.toLowerCase("Hello World!"))

# Complexity

# Time: O(n)

# Space: O(n)
