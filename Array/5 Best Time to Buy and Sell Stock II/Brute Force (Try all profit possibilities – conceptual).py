class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    profit = max(profit, prices[j] - prices[i])

        return profit


# ⏱ Time Complexity
# O(n²) ❌

# 📦 Space Complexity
# O(1)

# ❌ Will TLE
# ❌ Not interview-acceptable