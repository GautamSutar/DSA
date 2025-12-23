class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        n = len(prices)
        profit = 0

        while i < n - 1:
            # find valley
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy = prices[i]

            # find peak
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            sell = prices[i]

            profit += sell - buy

        return profit


# ⏱ Time Complexity
# O(n)

# 📦 Space Complexity
# O(1)

# ✔️ Correct
# ❌ Slightly complex logic