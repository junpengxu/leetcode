class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        profile = 0
        buy = prices[0]
        for i in range(len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            if prices[i] - buy > profile:
                profile = prices[i] - buy
        return profile