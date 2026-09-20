class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #no idea how to write it
        #data reps price fluctuation, so its ordered (assumed)
        #we should make a sliding window here, maybe fixed
        #check within the window for a, b if the following element subtracted sum is negative, that means there is a profit yield. otherwise we dont really care since that means theres just price dropping


        #conceptually
        maxProfits = 0
        cheapestBuy = prices[0]

        for i in range (len(prices)):
            #walk thru and set new min aka cheapestbuy
            if prices[i] < cheapestBuy:
                cheapestBuy = prices[i]

            currentProfit = prices[i] - cheapestBuy
        
            if currentProfit > maxProfits:
                maxProfits = currentProfit
        
        return maxProfits



