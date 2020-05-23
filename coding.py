class Solution:
    def maxProfit(self, prices):
        max_k = 2

        dp_0 = [[0 for i in range(max_k)] for i in prices]
        dp_1 = [[-prices[0] for i in range(max_k)] for i in prices]

        for i in range(len(prices)):
            for k in range(max_k):
                if i == 0: continue
                dp_0[i][k] = max(dp_0[i - 1][k], dp_1[i - 1][k] + prices[i])
                dp_1[i][k] = max(dp_1[i - 1][k], dp_0[i][k - 1] - prices[i])
        return dp_0[len(prices) - 1][max_k - 1]


if __name__ == '__main__':
    A = Solution()
    print(A.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
