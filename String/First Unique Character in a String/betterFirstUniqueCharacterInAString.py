class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
ob = Solution()
print(ob.firstUniqChar("aabb"))

# | Approach      | Time  | Space           |
# | ------------- | ----- | --------------- |
# | Frequency Map | O(n)  | O(1) (26 chars) |
