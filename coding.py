class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        result = [[0 for _ in range(m)] for _ in range(n)]
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]: return 0
        result[0][0] = 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]:
                    result[i][j] = 0
                elif i == 0:  # 不能直接赋值, 要判断下这个点可以不可以走过去
                    result[i][j] = 1 if (result[i][j - 1]) else 0
                elif j == 0:
                    result[i][j] = 1 if (result[i - 1][j]) else 0
                else:
                    result[i][j] = result[i - 1][j] + result[i][j - 1]
        return result[-1][-1]



if __name__ == '__main__':
    A = Solution()

    nums = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(A.uniquePathsWithObstacles(nums))
