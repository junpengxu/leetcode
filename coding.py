from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        memory = set()
        matrix_x = len(matrix)
        matrix_y = len(matrix[0])
        move = (0, 0)
        memory.add((0, 0))
        result = [matrix[0][0]]
        while True:
            if len(memory) >= matrix_x * matrix_y:
                return result
            for direct in directs:
                while True:
                    move = (move[0] + direct[0], move[1] + direct[1])

                    if not (move[0] >= 0 and move[0] < matrix_x and move[1] >= 0 and move[1] < matrix_y):
                        move = (move[0] - direct[0], move[1] - direct[1])
                        break

                    if move not in memory:
                        memory.add(move)
                        result.append(matrix[move[0]][move[1]])
                    else:
                        move = (move[0] - direct[0], move[1] - direct[1])
                        break


if __name__ == '__main__':
    A = Solution()
    print(A.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(A.spiralOrder(matrix=[]))
    print(A.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
