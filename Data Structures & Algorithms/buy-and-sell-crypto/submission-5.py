class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        cheapestBuy = prices[0]

        for i in range(len(prices)):
            if prices[i] < cheapestBuy:
                cheapestBuy = prices[i]

            if prices[i] - cheapestBuy > maxProfit:
                maxProfit = prices[i] - cheapestBuy
        return maxProfit
            