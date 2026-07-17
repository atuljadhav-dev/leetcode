class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        min=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min:
                min=prices[i]
            profit=prices[i]-min
            maxProfit=max(maxProfit,profit)
        return maxProfit