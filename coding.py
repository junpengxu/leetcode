from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)


if __name__ == '__main__':
    A = Solution()
    # print(A.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    # print(A.minCostClimbingStairs([0, 0, 0, 1]))
    print(A.minCostClimbingStairs([10, 15, 20, 20, 1, 18, 20]))
