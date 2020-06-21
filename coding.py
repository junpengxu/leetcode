class Solution:
    def generate_fac(self, n):
        result = []
        def dfs(rest, res):
            if not rest:
                result.append(res)
                return
            for item in range(len(rest)):
                dfs(rest[:item]+rest[item+1:], res + str(rest[item]))

        dfs([i for i in range(1, n + 1)], '')
        return result


if __name__ == '__main__':
    A = Solution()
    print(A.generate_fac(3))
