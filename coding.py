from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        pre, pre_pre = max(nums[:2]), nums[0]
        for index in range(2, len(nums)):
            pre, pre_pre = max(pre, pre_pre + nums[index]), pre
        return pre


if __name__ == '__main__':
    A = Solution()
    print(A.rob(nums=[2, 7, 9, 3, 1]))
    print(A.rob(nums=[1, 2, 3, 1]))
