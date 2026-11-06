class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        n = len(prices)

        for i in range(n):
            mini = float('inf')
            for j in range(i):
                mini = min(mini, prices[j])

            if prices[i] - mini > 0:
                profit.append(prices[i] - mini)

        return max(profit) if profit else 0