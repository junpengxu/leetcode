class Solution:
    def canJump(self, nums):
        dp = [False for _ in nums]
        dp[0] = True
        for i in range(len(nums)):
            if dp[i]:
                end = i + nums[i] + 1
                for j in range(i + 1, end):
                    if j >= len(nums): return True
                    dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    A = Solution()
    print(A.canJump())
