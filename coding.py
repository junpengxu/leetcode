class Solution():
    def mySqrt(self, x):
        if x == 0:
            return 0
        x0, C = float(x), float(x)
        while True:
            x = 0.5 * (x0 + C / x0)
            if abs(x0 - x) < 1e-7:
                break
            x0 = x
        return int(x)


if __name__ == '__main__':
    A = Solution()
    print(A.mySqrt(8))
    print(A.mySqrt(4))
