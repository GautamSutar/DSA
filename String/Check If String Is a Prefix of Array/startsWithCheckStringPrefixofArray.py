class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        temp = ""

        for word in words:
            temp += word
            if s.startswith(temp):
                if temp == s:
                    return True
            else:
                return False

        return False
ob = Solution()
print(ob.isPrefixString("iloveleetcode", ["i","love","leetcode","apples"]))



# | Approach        | Extra Space | Interview Rating |
# | --------------- | ----------- | ---------------- |
# | Concatenate     | O(n)        | ⭐⭐⭐          |
# | Join Prefix     | O(n)        | ⭐⭐⭐⭐        |
# | Character Match | O(1)        | ⭐⭐⭐⭐⭐      |
# | startswith      | O(n)        | ⭐⭐⭐⭐         |
