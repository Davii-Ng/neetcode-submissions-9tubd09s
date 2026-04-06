class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 , 1
        res = 0
        while l < r and r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                print(prices[l], prices[r], res)
                res = max(res, prices[r] - prices[l])
            r += 1
        return res


        