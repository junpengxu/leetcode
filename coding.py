class Solution:
    def generateMatrix(self, n: int):
        if not n: return
        maxtrix = [[0 for _ in range(n)] for _ in range(n)]

        def valid(node):
            x, y = node
            if 0 <= x and x < n and 0 <= y and y < n:
                return True
            return False

        moves = {
            'right': lambda node: (node[0], node[1] + 1),
            'down': lambda node: (node[0] + 1, node[1]),
            'left': lambda node: (node[0], node[1] - 1),
            'up': lambda node: (node[0] - 1, node[1]),
        }

        # the way have move
        memeory = set()

        # the first init position
        maxtrix[0][0] = 1
        number = 2

        def dfs(node):
            memeory.add(node)
            for _, move in moves.items():
                # 如果下一个节点是有效的，并且没有走过
                while valid(move(node)) and move(node) not in memeory:
                    # 更新本节点数据
                    memeory.add(node)
                    node = move(node)
                    x, y = node
                    nonlocal number
                    # 更新路径
                    maxtrix[x][y] = number
                    number+=1

                if valid(node) and node not in memeory:
                    dfs(node)

        dfs((0, 0))
        return maxtrix


if __name__ == '__main__':
    A = Solution()
    print(A.generateMatrix(5))

