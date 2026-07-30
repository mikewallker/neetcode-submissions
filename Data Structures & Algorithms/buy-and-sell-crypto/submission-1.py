class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMin = 0
        currentProfit = 0
        oldMin = 0
        priceMinDiff = 0
        for i in range(len(prices)):
            # track currentMin
            # if update currentMin:
            # 1. if curProfit not zero, update currentProfit by currentProfit + difference between the new min and old min
            if i == 0:
                currentMin = prices[0]
                continue
            if prices[i] < currentMin:
                currentMin = prices[i]
            else:
                priceMinDiff = prices[i] - currentMin
                if (priceMinDiff > currentProfit):
                    currentProfit = priceMinDiff
        return currentProfit
            
        