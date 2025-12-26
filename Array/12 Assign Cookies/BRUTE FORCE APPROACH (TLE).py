class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        used = [False] * len(s)
        count = 0 
        for i in range(len(g)):
            for j in range(len(s)):
                if not used[j] and s[j] >= g[i]:
                    used[j] = True
                    count += 1
                    break
        return count 
    
# ⏱ Time Complexity
# O(n × m)

# Worst case: 30,000 × 30,000 ❌
# ❌ Why bad?

# Nested loops
# Rechecking cookies repeatedly