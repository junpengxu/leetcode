class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:  # 相同的情况就不用管了，因为题目是要求去重复
                continue
            index = n - 1
            for j in range(i + 1, n):
                a, b, c = nums[i], nums[j], -(nums[i] + nums[j])
                if c < b:  # 这种的c是不符合题意的
                    break
                while nums[index] > c and index > j +1 :  # 相同的情况就不用管了，因为题目是要求去重复
                    index -= 1
                if nums[index] == c and index > j:
                    ans.add((a, b, c))
        return ans


class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            index = n - 1
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                c = 0 - a - b
                if c < b:
                    break
                while nums[index] > c and index > j + 1:
                    index = index - 1
                if nums[index] == c and index > j:
                    ans.add((a, b, c))
        return list(ans)
