class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == n - 1 or j == m - 1:
                    result[i][j] = 1

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                result[i][j] = result[i][j+1]+result[i+1][j]
        return result[0][0]


if __name__ == '__main__':
    A = Solution()
    print(A.uniquePaths(7, 3))
