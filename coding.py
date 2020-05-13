class Solution:
    def searchRange(self, nums, target):
        return [self.searchLeft(nums, target), self.searchRight(nums, target)]

    def searchLeft(self, nums, target):
        if len(nums) == 0: return -1;

        left_index, right_index = 0, len(nums) - 1
        if nums[left_index] == target: return 0
        if nums[left_index] > target or nums[right_index] < target: return -1

        # so left end < target, right end >= target
        # we perform binary search
        while left_index + 1 < right_index:
            mid = (left_index + right_index) // 2
            if nums[mid] < target:
                left_index = mid
            else:
                right_index = mid

        if nums[right_index] == target:
            return right_index
        else:
            return -1

    def searchRight(self, nums, target):
        if len(nums) == 0: return -1;

        left_index, right_index = 0, len(nums) - 1
        if nums[right_index] == target: return len(nums) - 1
        if nums[left_index] > target or nums[right_index] < target: return -1

        # so left end <= target, right end > target
        # we perform binary search
        while left_index + 1 < right_index:
            mid = (left_index + right_index) // 2
            if nums[mid] <= target:
                left_index = mid
            else:
                right_index = mid

        if nums[left_index] == target:
            return left_index
        else:
            return -1


if __name__ == '__main__':
    A = Solution()
    A.searchRange([5, 7, 7, 8, 8, 10], 8)
