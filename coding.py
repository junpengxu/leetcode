class Solution:
    def combine(self, n: int, k: int):
        res = []

        def backtrace(i, k, tmp):

            if k == 0:
                res.append(tmp)
                return res
            for j in range(i, n + 1):
                backtrace(j + 1, k - 1, tmp + [j])

        backtrace(1, k, [])
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.combine(4, 2))
