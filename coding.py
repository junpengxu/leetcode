class Solution:
    def isValidSudoku(self, board):
        square_dict = {str(i) + '_' + str(j): [] for i in range(3) for j in range(3)}
        col_list = [[] for _ in range(9)]
        row_list = [[] for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[row])):
                item = board[row][col]
                index = str(row // 3) + '_' + str(col // 3)
                if item == '.':
                    continue
                elif item not in square_dict[index] \
                        and item not in col_list[col] \
                        and item not in row_list[row]:
                    square_dict[index].append(item)
                    col_list[col].append(item)
                    row_list[row].append(item)
                else:
                    return False
        return True

if __name__ == '__main__':
    A = Solution()
    data = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(A.isValidSudoku(data))
    data_2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(A.isValidSudoku(data_2))