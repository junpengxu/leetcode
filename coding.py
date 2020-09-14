from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2  # left + (right - left) / 2 ,有效防止了 left 和 right 太大直接相加导致溢出
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = right - 1
        return -1


if __name__ == '__main__':
    A = Solution()
    print(A.search([-1, 0, 3, 5, 9, 12], -1))
