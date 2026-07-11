class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices) and l <= r:
            if prices[r] - prices[l] >= 0:
                maxProfit = max(maxProfit,prices[r] - prices[l])
            else:
                l = r
            r += 1

        return maxProfit

            
