class Solution:
    def firstMissingPositive(self, nums):
        nums = [item for item in nums if item >0]
        nums.sort()
        for index in range(len(nums)+1):
            if index + 1 not in nums:
                return index + 1
        return 1


if __name__ == '__main__':
    A = Solution()
    print(A.firstMissingPositive([7, 8, 9, 11, 12]))
    print(A.firstMissingPositive([3, 4, -1, 1]))
    print(A.firstMissingPositive([1, 2, 3]))
    print(A.firstMissingPositive([1, 2, 3, -1]))
    print(A.firstMissingPositive([-1, -2, -3]))
