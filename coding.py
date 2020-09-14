from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        return [self.search_left(nums, target), self.search_right(nums, target)]

    def search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        if target < nums[0]: return -1
        while left < right:
            mid = (left + right) // 2  # left + (right - left) / 2 ,有效防止了 left 和 right 太大直接相加导致溢出
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1

    def search_right(self, nums, target):
        left, right = 0, len(nums) - 1
        if target > nums[-1]: return -1
        while left <= right:
            mid = (left + right) // 2  # left + (right - left) / 2 ,有效防止了 left 和 right 太大直接相加导致溢出
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right if nums[right] == target else -1


if __name__ == '__main__':
    A = Solution()
    print(A.searchRange([1, 2, 2, 2, 2, 4, 4, 4, 4], 1))
