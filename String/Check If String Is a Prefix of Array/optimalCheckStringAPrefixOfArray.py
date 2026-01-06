class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        for word in words:
            prefix += word
            if prefix == s:
                return True
            # Optimization: if prefix length exceeds s, it can't be a prefix
            if len(prefix) > len(s):
                return False
        return False


ob = Solution()
print(ob.isPrefixString("a", ["aa", "aaaa", "banana"]))
# ⏱️ Complexity

# Time: O(n) (total characters)

# Space: O(1) ✅

# 🟢 Most preferred in interviews
