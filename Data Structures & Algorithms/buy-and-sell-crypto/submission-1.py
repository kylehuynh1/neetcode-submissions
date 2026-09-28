class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #there is no fixed size here... dynamic window approach ?

        low, best = 0, 0
        for r in range(1, len(prices)):
            #if current examined price is < buying price
            #update buying day index
            if prices[r] < prices[low]:
                low = r 
            else:
                best = max(best, prices[r] - prices[low])
        return best