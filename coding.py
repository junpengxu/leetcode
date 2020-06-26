class Solution():
    def removeDuplicates(self, nums):
        index = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[index]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[index] = nums[i]
                index += 1
        return index

if __name__ == '__main__':
    A = Solution()
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4]
    print(A.removeDuplicates(nums))
    print(nums)
