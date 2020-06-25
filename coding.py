class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        zero_position_set = set()

        def add_zero_position(x, y):
            # 返回所有需要被设置为0的坐标位置
            for i in range(m):
                zero_position_set.add((i, y))
            for i in range(n):
                zero_position_set.add((x, i))

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    add_zero_position(i, j)
        for i, j in zero_position_set:
            matrix[i][j] = 0

        return matrix


if __name__ == '__main__':
    A = Solution()
    # nums = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    nums = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
    print(A.setZeroes(nums))
