class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, best = 0, 0

        for r in range (1, len(prices)):
            if prices[r] < prices[low]:
                low = r
            else:
                best = max(best, prices[r] - prices[low])
        return best