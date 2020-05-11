class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        self.aim = -1
        self.binarysearch(nums, left, right, target)
        return self.aim

    def binarysearch(self, nums, left, right, target):

        mid = (left + right) // 2
        if nums[mid] == target:
            self.aim = mid
            return
        elif nums[left] == target:
            self.aim = left
            return
        elif nums[right] == target:
            self.aim = right
            return
        if right - left > 1 and self.aim == -1:
            self.binarysearch(nums, mid + 1, right, target)
            self.binarysearch(nums, left, mid - 1, target)


if __name__ == '__main__':
    A = Solution()
    print(A.search([1, 2], 2))
