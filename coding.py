class Solution:
    def generateParenthesis(self, n):
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return res
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        # 左括号比右括号少的情况下才增右括号
        if right > 0:
            self.dfs(res, left, right - 1, path + ')')


if __name__ == '__main__':
    Solution().generateParenthesis(3)
