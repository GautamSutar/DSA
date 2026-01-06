class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        temp = ""
        for word in words:
            temp += word 
            if temp == s:
                return True
            if len(temp) > len(s):
                return False
        return False
    
ob = Solution()
print(ob.isPrefixString("iloveleetcode", ["i","love","leetcode","apples"]))   

# ⏱️ Complexity

# Time: O(n) (total characters)

# Space: O(n) (temp string)