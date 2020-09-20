from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        fst_buy, fst_sell = float('-inf'), 0
        sec_buy, sec_sell = float('-inf'), 0
        for price in prices:
            fst_buy = max(fst_buy, -price)
            fst_sell = max(fst_sell, fst_buy + price)
            sec_buy = max(fst_sell - price, sec_buy)
            sec_sell = max(sec_sell, sec_buy + price)

        return sec_sell


if __name__ == '__main__':
    A = Solution()
    print(A.maxProfit([7, 1, 5, 3, 6, 4]))
