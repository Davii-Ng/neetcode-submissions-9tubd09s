class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            low = prices[i]
            for j in range(i+1,len(prices)):
                high = prices[j]
                print(high, low, res)
                res = max(res, high-low)
        return res


        