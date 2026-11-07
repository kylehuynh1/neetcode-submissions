class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0 #track max profit made
        cheapestBuy = prices[0] #lowest price

        #iterate through prices arr
        for i in range(len(prices)):
            
            #if theres a day with a cheaper price,
            #change the buying day to the current item at price[i]
            if prices[i] < cheapestBuy:
                cheapestBuy = prices[i]

            #current profit = current price (prices[i]) - cheapestbuy
            #if its larger than maxProfit,
            if (prices[i] - cheapestBuy) > maxProfit:
                #update maxprofit to reflect the current profit
                maxProfit = prices[i] - cheapestBuy
        return maxProfit #return maxprofit at the end