class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0] * n
        
        for i, v in enumerate(edges):
            score[v] += i
        
        max_score = -1
        ans = 0
        
        for i in range(n):
            if score[i] > max_score:
                max_score = score[i]
                ans = i
        
        return ans
