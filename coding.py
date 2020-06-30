class Solution:

    def exist(self, board, word):
        seen = set()
        self.board = board
        self.direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(index=(row, col), word=word, seen=seen):
                    return True
        return False

    def dfs(self, index, word, seen):
        row, col = index
        if not word:
            return True
        elif self.board[row][col] != word[0]:
            return False
        else:
            if len(word)==1:
                return True
            seen.add((row, col))
            for _row, _col in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if 0 <= _row < len(self.board) and 0 <= _col < len(self.board[0]) and (_row, _col) not in seen:
                    if self.dfs(index=(_row, _col), word=word[1:], seen=seen):
                        return True
            seen.remove((row, col))



[(1, 1,), (1, 0), (2, 0)]
if __name__ == '__main__':
    A = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print(A.exist(board, word))
    word = "ABCCED"
    print(A.exist(board, word))
    word = "ABCB"
    print(A.exist(board, word))

    board = [["a", "b"], ["c", "d"]]
    word = "bacd"
    print(A.exist(board, word))

    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    print(A.exist(board, word))

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    print(A.exist(board, word))
