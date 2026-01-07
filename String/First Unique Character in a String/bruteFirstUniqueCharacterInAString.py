class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in range(len(s)):
            count = 0
            for j in range(len(s)):
                if i != j and s[j] == s[i]:
                    count += 1
                    break
            if count == 0:
                return i
        return -1

ob = Solution()
print(ob.firstUniqChar("aabb"))
