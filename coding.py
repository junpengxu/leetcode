class Solution:
    def removeElement(self, nums, val):
        flag = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[flag] = nums[i]
                flag += 1
        return nums[:flag + 1]


if __name__ == '__main__':
    A = Solution()
    nums = [0, 0, 1, 1, 1, 2, 0, 2, 3, 3, 4]
    aa = A.removeElement(nums, 0)
    print(aa)


