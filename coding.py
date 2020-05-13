import bisect
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        return bisect.bisect_left(nums, target)


if __name__ == '__main__':
    A = Solution()
    assert A.searchInsert([1, 5, 5, 5, 5, 5, 5, 5, 5], 4) == 1
    assert A.searchInsert([1, 5, 5, 5, 5, 5, 5, 5, 5], 5) == 1
    assert A.searchInsert([1, 5, 5, 5, 5, 5, 5, 5, 5], 1) == 0
    assert A.searchInsert([1], 4) == 1
    assert A.searchInsert([1], 1) == 0
    assert A.searchInsert([1], 0) == 0
    assert A.searchInsert([1, 3], 0) == 0
    assert A.searchInsert([1, 3], 2) == 1
    assert A.searchInsert([1, 3], 4) == 2

