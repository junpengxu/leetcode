class Solution:
    def maxProfit(self, prices):
        total = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                total += profit
        return total


if __name__ == '__main__':
    A = Solution()
    A.maxProfit([7, 1, 5, 3, 6, 4])
