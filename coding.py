from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or not k:
            return 0

        max_k = k if k<=len(prices)//2 else len(prices)//2

        dp_0 = [[0 for i in range(max_k)] for i in prices]
        dp_1 = [[float('-inf') for i in range(max_k)] for i in prices]

        for i in range(len(prices)):
            for k in range(max_k):
                dp_0[i][k] = max(dp_0[i - 1][k], dp_1[i - 1][k] + prices[i])
                if k == 0:
                    dp_1[i][k] = max(dp_1[i - 1][k], - prices[i])
                else:
                    dp_1[i][k] = max(dp_1[i - 1][k], dp_0[i][k - 1] - prices[i])
        return dp_0[len(prices) - 1][max_k - 1]


if __name__ == '__main__':
    A = Solution()
    print(A.maxProfit(1, [1]))
