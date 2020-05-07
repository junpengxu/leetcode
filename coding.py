class Solution:
    def removeDuplicates(self, nums):
        flag = 0  # 不重复元素应该在的坐标
        for i in range(1, len(nums)):
            if nums[i] == nums[flag]:
                continue
            flag += 1
            if nums[i] != nums[flag]:
                nums[flag] = nums[i]
        return nums[:flag + 1]


if __name__ == '__main__':
    A = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    aa = A.removeDuplicates(nums)
    print(aa)
