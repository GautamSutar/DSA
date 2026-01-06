class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        length = 0
        k = 0

        for word in words:
            length += len(word)
            k += 1
            if length >= len(s):
                break

        return "".join(words[:k]) == s
ob = Solution()
print(ob.isPrefixString("iloveleetcode", ["i","love","leetcode","apples"]))


# ⏱️ Complexity

# Time: O(n)

# Space: O(n)