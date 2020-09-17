from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 定义dp 方程
        #dp[i][0] 代表第i天手中没有股票，此时的最大利润
        # 前一天没持有股票， 前一天持有股票（要标记为交易过）并且今天卖出
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[-1][1] = float('-inf')
        for i in range(len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(- prices[i], dp[i-1][1])
        return dp[-1][0]

if __name__ == '__main__':
    A= Solution()
    print(A.maxProfit([7,1,5,3,6,4]))