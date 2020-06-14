class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        dimension = len(matrix)
        for i in range(dimension):
            for j in range(i, dimension):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(dimension):
            for j in range((dimension // 2)):
                matrix[i][j], matrix[i][dimension - j - 1] = matrix[i][dimension - j - 1], matrix[i][j]


if __name__ == '__main__':
    A = Solution()
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    print(A.rotate(matrix))
