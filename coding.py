from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(tmp, nums):
            result.append(tmp)
            if not nums:
                return
            for i in range(len(nums)):
                helper(tmp + [nums[i]], nums[i + 1:])

        helper([], nums)
        return result


if __name__ == '__main__':
    A = Solution()
    print(A.subsets([1, 2, 3, 4, 5]))
