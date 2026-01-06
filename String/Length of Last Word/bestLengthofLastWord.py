class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        for ch in s:
            if ch != " ":
                count += 1
            else:
                if count > 0:
                    last = count
                    print (last)
                count = 0

        return count if count > 0 else last

ob = Solution()
print(ob.lengthOfLastWord("    day   "))

# ⏱️ Complexity

# Time: O(n)

# Space: O(1)