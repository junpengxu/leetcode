from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 定义dp 方程
        # dp[i][0] 代表第i天手中没有股票，此时的最大利润
        # 前一天没持有股票， 前一天持有股票（要标记为交易过）并且今天卖出
        if not prices:
            return 0
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        for i in range(len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(tmp -prices[i], dp_i_1)
        return dp_i_0


if __name__ == '__main__':
    A = Solution()
    print(A.maxProfit([7, 1, 5, 3, 6, 4]))
