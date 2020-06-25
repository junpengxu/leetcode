class Solution:
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        result = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    result[0][0] = grid[0][0]
                elif i == 0:
                    result[i][j] = grid[i][j] + result[i][j - 1]
                elif j == 0:
                    result[i][j] = grid[i][j] + result[i - 1][j]
                else:
                    result[i][j] = grid[i][j] + min(result[i - 1][j], result[i][j - 1])
        return result[-1][-1]


if __name__ == '__main__':
    A = Solution()

    nums = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(A.minPathSum(nums))
